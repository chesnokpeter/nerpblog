from nerpblog.app.services import UserServices
from nerpblog.app.db.controller import UserController
from nerpblog.app.services import PostServices
from nerpblog.app.db.controller import PostController

from nerpblog.app.db import session



def depends_user():
    controller = UserController(session)
    return UserServices(controller)

def depends_post():
    controller = PostController(session)
    return PostServices(controller)

