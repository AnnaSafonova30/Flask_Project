from .settings import project
from tour import tour_app, show_tour


tour_app.add_url_rule(
    rule = "/",
    view_func = show_tour,
    methods = ["GET", "POST"]
)