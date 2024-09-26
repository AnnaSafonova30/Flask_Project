import flask

home_app = flask.Blueprint(
    name = "home_app",
    import_name = "home_app",
    static_folder = "station",
    static_url_path = "/station/",
    template_folder = "templates"
)