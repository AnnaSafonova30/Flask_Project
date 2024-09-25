import flask 

project = flask.Flask(
    import_name = "core",
    template_folder = "templates",
    static_folder = "static",
    static_url_path = "/static/"
)