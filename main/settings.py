import flask 

project = flask.Flask(
    import_name = "core",
    template_folder = "main/templates",
    static_folder = "static",
    static_url_path = "/static/"
)