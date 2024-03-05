from nerpblog.app.db.controller import CommentController, PostController, UserController, AbsController
from nerpblog.app.db import async_session_maker
from abc import ABC, abstractmethod
from typing import Type

class AbsUnitOfWork(ABC):
    user = Type[UserController]
    comment = Type[CommentController]
    post = Type[PostController]
    @abstractmethod
    def __init__(self): raise NotImplementedError
    @abstractmethod
    async def __aenter__(self): raise NotImplementedError
    @abstractmethod
    async def __aexit__(self, *args): raise NotImplementedError
    @abstractmethod
    async def commit(self): raise NotImplementedError
    @abstractmethod
    async def rollback(self): raise NotImplementedError


class UnitOfWork:
    def __init__(self):
        self.session_factory = async_session_maker

    async def __aenter__(self):
        self.session = self.session_factory()

        self.user = UserController(self.session)
        self.comment = CommentController(self.session)
        self.post = PostController(self.session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()