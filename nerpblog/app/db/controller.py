from typing import List, Any

from sqlalchemy.orm import Session

from nerpblog.app.db.tables import USER, POST
from nerpblog.app.models import UserModel, PostModel

class UserController:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_user(self, **data) -> List[UserModel]:
        q = self.session.query(USER).filter_by(**data).all() 
        r = []
        if not q: return r
        for i in q: r.append(i.get_attributes_dict())
        return r

    def login_user(self, **data) -> UserModel:
        user = USER(**data)
        self.session.add(user)
        self.session.commit()
        return user.get_attributes_dict()
    



class PostController:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_user(self, **data) -> UserModel:
        q = self.session.query(USER).filter_by(**data).one_or_none() 
        return q

    def new_post(self, **data) -> PostModel:
        post = POST(**data)
        self.session.add(post)
        self.session.commit()
        return post.get_attributes_dict()

    def get_posts(self, offset: int = 0, limit: int = 10) -> List[PostModel]:
        q = self.session.query(POST).order_by(POST.id.desc()).offset(offset).limit(limit).all()
        r = []
        for i in q:
            r.append(i.get_attributes_dict())
        return r

    def get_one_post(self, **data) -> PostModel:
        q = self.session.query(POST).filter_by(**data).one_or_none()
        if not q: return q
        return q.get_attributes_dict()

    def add_like(self, **data) -> PostModel:
        q = self.session.query(POST).filter_by(**data).one_or_none()
        if not q: return q
        q.likes = q.likes+1
        self.session.commit()
        return q.get_attributes_dict()

    def remove_like(self, **data) -> PostModel:
        q = self.session.query(POST).filter_by(**data).one_or_none()
        if not q: return q
        q.likes = q.likes-1
        self.session.commit()
        return q.get_attributes_dict()