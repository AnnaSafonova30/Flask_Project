import flask, flask_sqlalchemy, flask_migrate
import os
from flask_mail import *
project = flask.Flask(
    import_name = "core",
    template_folder = "main/templates",
    static_folder = "static",
    static_url_path = "/static/",
    instance_path = os.path.abspath(__file__ + "/../../instance")
)

project.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

database = flask_sqlalchemy.SQLAlchemy(app = project)

migrate = flask_migrate.Migrate(app = project, db = database)


project.config['MAIL_SERVER'] = 'smtp.gmail.com'
project.config['MAIL_PORT'] = 465
project.config['MAIL_USERNAME'] = 'zx00xsanyazx@gmail.com' 
project.config['MAIL_PASSWORD'] = "ukbi axgl ekyg kdwj"
project.config['MAIL_USE_TLS'] = False
project.config['MAIL_USE_SSL'] = True

mail = Mail(project)

