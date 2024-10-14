import flask
from main.settings import database 
from flask_login import UserMixin


class User(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key = True)
    username = database.Column(database.String(120), nullable = False)
    password = database.Column(database.String(120), nullable = False)
