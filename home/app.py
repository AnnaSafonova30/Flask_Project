import flask

home_app = flask.Blueprint(
    name = "home_app",
    import_name = "app",
    static_folder = "station",
    static_url_path = "/station/",
    template_folder = "home/templates"
)