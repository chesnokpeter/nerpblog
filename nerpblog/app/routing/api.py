from typing import Annotated
from fastapi import APIRouter, Depends

from nerpblog.app.depends import depends_post, depends_user, depends_comm
from nerpblog.app.services import PostServices, UserServices, CommentServices

from nerpblog.app.models import AddComment

apiRouter = APIRouter(prefix='/api', tags=['api'])

@apiRouter.get('/posts')
def getPostsList(services: Annotated[PostServices, Depends(depends_post)], offset: int = 0, limit: int = 10):
    return services.get_posts(offset=offset, limit=limit)

@apiRouter.get('/post/{id}')
def getPost(id: int, services: Annotated[PostServices, Depends(depends_post)]):
    return services.get_one_post(id=id)

@apiRouter.post('/like')
def addLike(id: int, services: Annotated[PostServices, Depends(depends_post)]):
    return services.add_like(id=id)

@apiRouter.post('/remlike')
def remLike(id: int, services: Annotated[PostServices, Depends(depends_post)]):
    return services.remove_like(id=id)

@apiRouter.post('/comm')
def addComm(comm: AddComment, services: Annotated[CommentServices, Depends(depends_comm)]):
    return services.add_comment(comm)


# @apiRouter.get('/speed')
# def speed(str: str):
#     return str

# @apiRouter.post('/addpost')
# def APIremlike(post: AddPost, services: Annotated[PostServices, Depends(depends_post)]):
#     return services.new_post(post)

# @apiRouter.post('/adduser')
# def APIremlike(tgid: int, services: Annotated[UserServices, Depends(depends_user)]):
#     return services.login_user(tgid=tgid, name='username', tglink='t.me/')
