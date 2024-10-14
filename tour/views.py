import flask
from flask_login import current_user
from user.models import User

def show_tour():
    return flask.render_template(template_name_or_list = "tour.html", is_auth = current_user.is_authenticated,
        user_data = User.query.get(current_user.id) if current_user.is_authenticated else None)