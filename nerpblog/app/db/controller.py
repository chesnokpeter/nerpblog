from typing import List, Any, Type
from sqlalchemy.orm import Session
from sqlalchemy import select, update
from nerpblog.app.db.models import USER, POST, COMMENT, AbsMODEL, Base

from abc import ABC, abstractmethod, abstractproperty

class AbsController(ABC):
    model: AbsMODEL
    @abstractmethod
    def __init__(self): raise NotImplementedError
    @abstractmethod
    async def get(self): raise NotImplementedError
    @abstractmethod
    async def get_one(self): raise NotImplementedError
    @abstractmethod
    async def offset(self): raise NotImplementedError
    @abstractmethod
    async def update(self): raise NotImplementedError


class Controller:
    model = AbsMODEL
    def __init__(self, session: Session):
        self.session = session
    async def get(self, **data) -> List[List[model]]:
        result = await self.session.execute(select(self.model).filter_by(**data))
        return result.all()
    async def get_one(self, **data) -> model:
        stmt = select(self.model).filter_by(**data)
        res = await self.session.execute(stmt)
        res = res.first()
        return res[0] if res else res
    # async def add(self, **data) -> model:
    #     c = self.model(**data)
    #     self.session.add(c)
    #     self.session.commit()
    #     return c.model()
    async def offset(self, offset: int = 0, limit: int = 10, order = None, **data) -> List[List[model]]:
        stmt = select(self.model).offset(offset).limit(limit)
        res = await self.session.execute(stmt)
        res = res.all()
        return res
    async def update(self, id: int, **data) -> model:
        query = (
            update(self.model)
            .where(self.model.id == id )
            .values(**data)
            .returning(self.model)
        ) 
        return await self.session.scalar(query)


class UserController(Controller):
    model = USER

class PostController(Controller):
    model = POST

class CommentController(Controller):
    model = COMMENT


# class UserController:
#     def __init__(self, session: Session) -> None:
#         self.session = session

#     def get_user(self, **data) -> List[UserModel]:
#         q = self.session.query(USER).filter_by(**data).all() 
#         it = 0
#         for i in q: q[it] = i.model();it+=1 
#         return q

#     def login_user(self, **data) -> UserModel:
#         user = USER(**data)
#         self.session.add(user)
#         self.session.commit()
#         return user.model()

# class PostController:
#     def __init__(self, session: Session) -> None:
#         self.session = session

#     def get_user(self, **data) -> UserModel:
#         q = self.session.query(USER).filter_by(**data).one_or_none() 
#         return q.model()

#     def new_post(self, **data) -> PostModel:
#         post = POST(**data)
#         self.session.add(post)
#         self.session.commit()
#         return post.model()

#     def get_posts(self, offset: int = 0, limit: int = 10) -> List[PostModel]:
#         q = self.session.query(POST).order_by(POST.id.desc()).offset(offset).limit(limit).all()
#         it = 0
#         for i in q: q[it] = i.model();it+=1
#         return q

#     def get_one_post(self, **data) -> PostModel:
#         q = self.session.query(POST).filter_by(**data).one_or_none()
#         return q.model() if q else {}

#     def add_like(self, **data) -> PostModel:
#         q = self.session.query(POST).filter_by(**data).one_or_none()
#         if not q: return {}
#         q.likes = q.likes+1
#         self.session.commit()
#         return q.model()

#     def remove_like(self, **data) -> PostModel:
#         q = self.session.query(POST).filter_by(**data).one_or_none()
#         if not q: return q
#         q.likes = q.likes-1
#         self.session.commit()
#         return q.model()
    
#     def posts_by(self, offset: int = 0, limit: int = 10, **data) -> List[PostModel]:
#         q = self.session.query(POST).order_by(POST.id.desc()).filter_by(**data).offset(offset).limit(limit).all()
#         it = 0
#         for i in q: q[it] = i.model();it+=1
#         return q

# class CommentController:
#     def __init__(self, session: Session) -> None:
#         self.session = session
    
#     def get_user(self, **data) -> UserModel:
#         q = self.session.query(USER).filter_by(**data).one_or_none() 
#         return q

#     def get_post(self, **data) -> PostModel:
#         q = self.session.query(POST).filter_by(**data).one_or_none() 
#         return q

#     def add_comment(self, **data) -> CommentModel:
#         comment = COMMENT(**data)
#         self.session.add(comment)
#         self.session.commit()
#         return comment.model()
    
#     def get_comments(self, **data) -> List[CommentModel]:
#         q = self.session.query(COMMENT).filter_by(**data).order_by(COMMENT.id.desc()).all()
#         it = 0
#         for i in q: q[it] = i.model();it+=1
#         return q
    