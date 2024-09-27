import home
from .settings import project

home.home_app.add_url_rule(
    rule = "/",
    view_func = home.show_home_list
)
project.register_blueprint(blueprint = home.home_app)