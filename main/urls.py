import home
import tour
import user
from .settings import project


home.home_app.add_url_rule(
    rule = "/",
    view_func = home.show_home_list,
    methods = ["GET", "POST"]
)
project.register_blueprint(blueprint = home.home_app)

tour.tour_app.add_url_rule(
    rule = "/tour",
    view_func = tour.show_tour,
    methods = ["GET", "POST"]
)
tour.tour_app.add_url_rule(
    rule = "/tour/<int:id>",
    view_func = tour.show_view_tour,
    methods = ["GET", "POST"]
)
project.register_blueprint(blueprint = tour.tour_app)

user.user_app.add_url_rule(
    rule = "/registration",
    view_func = user.registration_user_app,
    methods = ["GET", "POST"]
)
user.user_app.add_url_rule(
    rule = "/login",
    view_func = user.login_user_app,
    methods = ["GET", "POST"]
)

user.user_app.add_url_rule(
    rule = "/logout",
    view_func = user.logout,
    methods = ["GET", "POST"]
)
project.register_blueprint(blueprint = user.user_app)

