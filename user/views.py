import flask
from flask_login import login_user, current_user
from main.settings import database 
from .models import User


def registration_user_app():
    if flask.request.method == 'POST':
        
        users = User(
            username = flask.request.form["username"],
            password = flask.request.form["password"],
        )
        database.session.add(users)
        database.session.commit()
    return flask.render_template(template_name_or_list = "registration.html", 
        is_auth = current_user.is_authenticated, 
        user_data = User.query.get(current_user.id) if current_user.is_authenticated else None)


def login_user_app():
    if flask.request.method == "POST":
        username = flask.request.form["username"]
        password = flask.request.form["password"]
        for user in User.query.filter_by(username = username):
            if user.password == password:
                login_user(user)
                flask.redirect("/")
                break
    
    return flask.render_template(
        template_name_or_list = "login.html",
        is_auth = current_user.is_authenticated,
        user_data = User.query.get(current_user.id) if current_user.is_authenticated else None)