from flask import Flask
from flask_admin import Admin, AdminIndexView, expose
from flask_basicauth import BasicAuth

from nerpblog.app.db.tables import USER, POST, COMMENT
from nerpblog.app.admin.views import PostView, CommentView, UserView

from nerpblog.app.db import session
from nerpblog.config import flask_secret_key, admin_username, admin_password

flask_app = Flask(__name__)
flask_app.config['SECRET_KEY'] = flask_secret_key
flask_app.config['BASIC_AUTH_USERNAME'] = admin_username
flask_app.config['BASIC_AUTH_PASSWORD'] = admin_password
flask_app.config['BASIC_AUTH_FORCE'] = True

basic_auth = BasicAuth(flask_app)

class AdminIndexView(AdminIndexView):
    @expose('/')
    @basic_auth.required
    def index(self):
        return self.render('index.html')


admin = Admin(flask_app, name='nerpblog admin', template_mode='bootstrap4', index_view=AdminIndexView(name='main', url='/'))

admin.add_view(UserView(USER, session))
admin.add_view(PostView(POST, session))
admin.add_view(CommentView(COMMENT, session))