import flask

def show_tour():
    return flask.render_template(template_name_or_list = "tour.html")