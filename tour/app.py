import flask

tour_app = flask.Blueprint(
    name = "tour",
    import_name = "app",
    template_folder = "tour/templates",
    static_folder = "static",
    static_url_path = "/static/" 
)