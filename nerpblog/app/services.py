from typing import List, Any, Union
from datetime import datetime

from nerpblog.app.db.controller import UserController, PostController, CommentController

from nerpblog.app.models import (
    UserModel, 
    PostModel, 
    AddPost, 
    AddPostExtended, 
    AddComment, 
    AddCommentExtended,
    PostExtended,
    CommentModel,
    CommentExtended
)
from nerpblog.config import bot_username, bot_start_deeplink
from nerpblog.app.db.tables import COMMENT, POST, USER
from nerpblog.app.schemas.post import PostSchema, Post_User
from nerpblog.app.uow import UnitOfWork
from aiogram.utils.deep_linking import create_deep_link

class UserServices:
    def __init__(self, controller: UserController) -> None:
        self.controller = controller

    def get_user(self, **data) -> List[UserModel]:
        return self.controller.get_one(**data)

    def login_user(self, tgid: int, name: str, tglink: str) -> dict[str, Union[str, UserModel]]:
        u = self.controller.get_user(tgid=tgid)
        if u: return {'type':'error','detail':'tgid already exist'}
        return {'type':'sucess', 'detail': self.controller.login_user(tgid=tgid,name=name, tglink=tglink)}



class PostServices:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def get_posts(self, offset: int = 0, limit: int = 10) -> List[PostSchema]:
        async with self.uow:
            r: List[POST] = await self.uow.post.offset(offset, limit)
            for i, v in enumerate(r): 
                u: USER = await self.uow.user.get_one(id=r.userid) #! last dumb
                r[i] = v[0].to_scheme()
            return r
    
    async def get_post(self, **data) -> Post_User:
        async with self.uow:
            r: POST = await self.uow.post.get_one(**data)
            if not r: return {}
            u: USER = await self.uow.user.get_one(id=r.userid)
            l = create_deep_link(bot_username, bot_start_deeplink, f'postid{r.id}', True)
            r = Post_User(**r.to_scheme().model_dump(), username=u.name, botlink=l)
            return r

    # def new_post(self, data: AddPost) -> dict[str, Union[str, UserModel]]:
    #     u = self.controller.get_user(id=data.userid)
    #     if not u: return {'type':'error','detail':'userid not found'}
    #     data = AddPostExtended(**data.model_dump(), date=datetime.now(), likes=0)
    #     return {'type':'sucess', 'detail': self.controller.new_post(**data.model_dump())}

    # def get_posts(self, offset: int = 0, limit: int = 10) -> List[PostExtended]:
    #     list = self.controller.get_posts(offset=offset, limit=limit)
    #     it = 0
    #     for i in list: 
    #         list[it] = PostExtended(**i.model_dump(), username=self.controller.get_user(id=i.userid).name);it+=1
    #     return list

    # def get_one_post(self, id: int) -> PostExtended:
    #     p = self.controller.get_one(id=id)
    #     if not p: return {}
    #     u = self.controller.get_one(id=p.userid).name
    #     l = create_deep_link('nrpblgbot', 'start', f'postid{p.id}', True)
    #     # p = PostExtended(**p.model_dump(), username=u, botlink=l)
    #     return p

    # def add_like(self, id: int) -> dict[str, Union[str, PostModel]]:
    #     l = self.controller.add_like(id=id)
    #     if not l: return {"type":"error",'detail':'post not found'}
    #     return {'type':'sucess','detail':l}

    # def remove_like(self, id: int) -> dict[str, Union[str, PostModel]]:
    #     l = self.controller.remove_like(id=id)
    #     if not l: return {"type":"error",'detail':'post not found'}
    #     return {'type':'sucess','detail':l}

    # def posts_by(self, offset: int = 0, limit: int = 10, **data) -> List[PostModel]:
    #     return self.controller.posts_by(offset=offset, limit=limit, **data)

class CommentServices:
    def __init__(self, controller: CommentController) -> None:
        self.controller = controller

    def add_comment(self, data: AddComment) -> CommentModel:
        p = self.controller.get_post(id=data.postid)
        if not p: return {'type':'error','detail':'postid not found'}
        u = self.controller.get_user(tgid=data.tgid)
        if not u: return {'type':'error','detail':'tgid not found'}
        data = AddCommentExtended(**data.model_dump(), date=datetime.now(), userid=u.id)
        data = data.model_dump()
        if data.get('tgid'): del data['tgid']
        return {'type':'sucess', 'detail': self.controller.add_comment(**data)}

    def get_comments(self, **data) -> List[CommentExtended]:
        list = self.controller.get_comments(**data)
        it = 0
        for i in list: list[it] = CommentExtended(**i.model_dump(), username=self.controller.get_user(id=i.userid).name);it+=1
        return list