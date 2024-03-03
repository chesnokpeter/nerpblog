from fastapi import APIRouter
from nerpblog.app.services import PostServices, CommentServices #UserServices, 
from nerpblog.app.schemas.comment import CommentSchema, CommentSchemaExtend
from nerpblog.app.schemas.post import PostSchema, PostSchemaExtend
from nerpblog.app.depends import uowdep
from typing import List

apiRouter = APIRouter(prefix='/api', tags=['api'])

@apiRouter.get('/posts', response_model=List[PostSchemaExtend], description='get posts list')
async def get_posts_list(uow: uowdep, offset: int = 0, limit: int = 10):
    return await PostServices(uow).get_posts(offset, limit)

@apiRouter.get('/post/{id}', response_model=PostSchemaExtend, description='get post by postid')
async def get_post(id: int, uow: uowdep): 
    return await PostServices(uow).one_post(id=id)

@apiRouter.get('/post/{id}/comments', response_model=List[CommentSchemaExtend], description='get comments list by postid')
async def get_comments_list(id: int, uow: uowdep):
    return await CommentServices(uow).get_comments(postid=id)

@apiRouter.post('/like', response_model=PostSchema, description='add +1 like post by postid')
async def add_like(uow: uowdep, id: int):
    return await PostServices(uow).add_like(id=id)

@apiRouter.post('/remlike', response_model=PostSchema, description='remove -1 like post by postid')
async def remove_like(uow: uowdep, id: int):
    return await PostServices(uow).rem_like(id=id)


# @apiRouter.get('/posts')
# def getPostsList(services: Annotated[PostServices, Depends(depends_post)], offset: int = 0, limit: int = 10):
#     return services.get_posts(offset=offset, limit=limit)

# @apiRouter.get('/post/{id}')
# def getPost(id: int, services: Annotated[PostServices, Depends(depends_post)]):
#     return services.get_one_post(id=id)

# @apiRouter.get('/post/{id}/comments')
# def getPost(id: int, services: Annotated[CommentServices, Depends(depends_comm)]):
#     return services.get_comments(postid=id)

# @apiRouter.post('/like')
# def addLike(id: int, services: Annotated[PostServices, Depends(depends_post)]):
#     return services.add_like(id=id)

# @apiRouter.post('/remlike')
# def remLike(id: int, services: Annotated[PostServices, Depends(depends_post)]):
#     return services.remove_like(id=id)




# @apiRouter.post('/comm')
# def addComm(comm: AddComment, services: Annotated[CommentServices, Depends(depends_comm)]):
#     return services.add_comment(comm)

# @apiRouter.post('/getcomm')
# def addComm(postid: int, services: Annotated[CommentServices, Depends(depends_comm)]):
#     return services.get_comments(postid=postid)

# @apiRouter.get('/speed')
# def speed(str: str):
#     return str

# @apiRouter.post('/addpost')
# def APIremlike(post: AddPost, services: Annotated[PostServices, Depends(depends_post)]):
#     return services.new_post(post)

# @apiRouter.post('/adduser')
# def APIremlike(tgid: int, services: Annotated[UserServices, Depends(depends_user)]):
#     return services.login_user(tgid=tgid, name='username', tglink='t.me/')
