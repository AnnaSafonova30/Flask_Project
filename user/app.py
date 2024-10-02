import flask

project_app = flask.Blueprint(
    import_name = "app",
    template_folder = "user/templates",
    static_folder = "static",
    static_url_path = "/static/"
)