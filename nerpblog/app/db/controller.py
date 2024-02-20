from typing import List, Any

from sqlalchemy.orm import Session

from nerpblog.app.db.tables import USER, POST, COMMENT
from nerpblog.app.models import UserModel, PostModel, CommentModel

class UserController:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_user(self, **data) -> List[UserModel]:
        q = self.session.query(USER).filter_by(**data).all() 
        it = 0
        for i in q: q[it] = i.model();it+=1 
        return q

    def login_user(self, **data) -> UserModel:
        user = USER(**data)
        self.session.add(user)
        self.session.commit()
        return user.model()

class PostController:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_user(self, **data) -> UserModel:
        q = self.session.query(USER).filter_by(**data).one_or_none() 
        return q.model()

    def new_post(self, **data) -> PostModel:
        post = POST(**data)
        self.session.add(post)
        self.session.commit()
        return post.model()

    def get_posts(self, offset: int = 0, limit: int = 10) -> List[PostModel]:
        q = self.session.query(POST).order_by(POST.id.desc()).offset(offset).limit(limit).all()
        it = 0
        for i in q: q[it] = i.model();it+=1
        return q

    def get_one_post(self, **data) -> PostModel:
        q = self.session.query(POST).filter_by(**data).one_or_none()
        return q.model() if q else {}

    def add_like(self, **data) -> PostModel:
        q = self.session.query(POST).filter_by(**data).one_or_none()
        if not q: return {}
        q.likes = q.likes+1
        self.session.commit()
        return q.model()

    def remove_like(self, **data) -> PostModel:
        q = self.session.query(POST).filter_by(**data).one_or_none()
        if not q: return q
        q.likes = q.likes-1
        self.session.commit()
        return q.model()

class CommentController:
    def __init__(self, session: Session) -> None:
        self.session = session
    
    def get_user(self, **data) -> UserModel:
        q = self.session.query(USER).filter_by(**data).one_or_none() 
        return q

    def get_post(self, **data) -> PostModel:
        q = self.session.query(POST).filter_by(**data).one_or_none() 
        return q

    def add_comment(self, **data) -> CommentModel:
        comment = COMMENT(**data)
        self.session.add(comment)
        self.session.commit()
        return comment.model()

    def get_comments(self, **data) -> List[CommentModel]:
        q = self.session.query(COMMENT).filter_by(**data).order_by(COMMENT.id.desc()).all()
        it = 0
        for i in q: q[it] = i.model();it+=1
        return q