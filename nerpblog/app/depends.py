from fastapi import Depends
from typing import Annotated
from nerpblog.app.uow import UnitOfWork

# from nerpblog.app.services import UserServices
# from nerpblog.app.db.controller import UserController
# from nerpblog.app.services import PostServices
# from nerpblog.app.db.controller import PostController
# from nerpblog.app.services import CommentServices
# from nerpblog.app.db.controller import CommentController

# from nerpblog.app.db import session

# ucontroller = UserController(session)
# pcontroller = PostController(session)
# ccontroller = CommentController(session)

def depends_user():
    # return UserServices(ucontroller)
    return ...

def depends_post():
    # return PostServices(pcontroller)
    return ...

def depends_comm():
    # return CommentServices(ccontroller)
    return ...



uowdep = Annotated[UnitOfWork, Depends(UnitOfWork)]