import flask_login
from .settings import project
from user.models import User


project.secret_key = "1234567890"

login_manager = flask_login.LoginManager(project)


@login_manager.user_loader
def load_user(id):
    return User.query.get(id)