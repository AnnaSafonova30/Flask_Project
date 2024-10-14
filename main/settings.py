import flask, flask_sqlalchemy, flask_migrate
import os

project = flask.Flask(
    import_name = "core",
    template_folder = "main/templates",
    static_folder = "static",
    static_url_path = "/static/",
      instance_path = os.path.abspath(__file__ + "/..")
)

project.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

database = flask_sqlalchemy.SQLAlchemy(app = project)

migrate = flask_migrate.Migrate(app = project, db = database)
