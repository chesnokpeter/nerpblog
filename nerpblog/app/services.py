from typing import List, Any, Union
from datetime import datetime

from nerpblog.app.db.controller import UserController, PostController

from nerpblog.app.models import UserModel, PostModel, AddPost, AddPostExtended

from aiogram.utils.deep_linking import create_deep_link



class UserServices:
    def __init__(self, controller: UserController) -> None:
        self.controller = controller

    def get_user(self, **data) -> List[UserModel]:
        return self.controller.get_user(**data)

    def login_user(self, tgid: int, name: str, tglink: str) -> dict[str, Union[str, UserModel]]:
        u = self.controller.get_user(tgid=tgid)
        if u: return {'type':'error','detail':'tgid already exist'}
        return {'type':'sucess', 'detail': self.controller.login_user(tgid=tgid,name=name, tglink=tglink)}



class PostServices:
    def __init__(self, controller: PostController) -> None:
        self.controller = controller

    def new_post(self, data: AddPost) -> dict[str, Union[str, UserModel]]:
        u = self.controller.get_user(id=data.userid)
        if not u: return {'type':'error','detail':'userid not found'}
        data = AddPostExtended(**data.model_dump(), date=datetime.now(), likes=0)
        return {'type':'sucess', 'detail': self.controller.new_post(**data.model_dump())}

    def get_posts(self, offset: int = 0, limit: int = 10) -> List[PostModel]:
        list = self.controller.get_posts(offset=offset, limit=limit)
        if not list: return list
        r = []
        for i in list:
            d = i.model_dump()
            d['username'] = self.controller.get_user(id=i.userid).name
            r.append(d)
        return r

    def get_one_post(self, id: int) -> PostModel:
        p = self.controller.get_one_post(id=id)
        if not p: return {}
        u = self.controller.get_user(id=p.userid).name
        l = create_deep_link('nrpblgbot', 'start', f'postid{p.id}', True)
        p = p.model_dump()
        p['username'] = u
        p['botlink'] = l
        return p

    def add_like(self, id: int) -> dict[str, Union[str, UserModel]]:
        l = self.controller.add_like(id=id)
        if not l: return {"type":"error",'detail':'post not found'}
        return {'type':'sucess','detail':l}

    def remove_like(self, id: int) -> dict[str, Union[str, UserModel]]:
        l = self.controller.remove_like(id=id)
        if not l: return {"type":"error",'detail':'post not found'}
        return {'type':'sucess','detail':l}

