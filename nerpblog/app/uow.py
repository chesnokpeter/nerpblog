from nerpblog.app.db.controller import CommentController, PostController, UserController
from nerpblog.app.db import async_session_maker



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