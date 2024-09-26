import flask

def show_home_list():
    return flask.render_template(template_name_or_list = "home.html")