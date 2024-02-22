from flask import Flask
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView

from nerpblog.app.db.tables import USER, POST, COMMENT
from nerpblog.app.db import session

from nerpblog.app.admin.views import PostView, CommentView, UserView

from nerpblog.config import flask_secret_key

flask_app = Flask(__name__)
flask_app.config['SECRET_KEY'] = flask_secret_key


admin = Admin(flask_app, name='nerpblog admin', template_mode='bootstrap4', index_view=AdminIndexView(name='main', url='/'))
admin.add_view(UserView(USER, session))
admin.add_view(PostView(POST, session))
admin.add_view(CommentView(COMMENT, session))