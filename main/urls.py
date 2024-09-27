import home
import tour
from .settings import project

home.home_app.add_url_rule(
    rule = "/",
    view_func = home.show_home_list
)
project.register_blueprint(blueprint = home.home_app)

tour.tour_app.add_url_rule(
    rule = "/tour",
    view_func = tour.show_tour,
    methods = ["GET", "POST"]
)
project.register_blueprint(blueprint = tour.tour_app)