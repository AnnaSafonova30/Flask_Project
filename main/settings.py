import flask 
from flask_mail import *
project = flask.Flask(
    import_name = "core",
    template_folder = "main/templates",
    static_folder = "static",
    static_url_path = "/static/"
)

project.config['MAIL_SERVER'] = 'smtp.gmail.com'
project.config['MAIL_PORT'] = 465
project.config['MAIL_USERNAME'] = 'yourproject@gmail.com' 
project.config['MAIL_PASSWORD'] = 'yourpassword' 
project.config['MAIL_USE_TLS'] = False
project.config['MAIL_USE_SSL'] = True

mail = Mail(project)

