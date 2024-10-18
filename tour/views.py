import flask
from flask_login import current_user
from user.models import User
from .models import Tour
from main.settings import DATABASE
import os


def show_tour():
    
    # product = Tour(
    #     title = "Крим",
    #     date = "12.05.2025",
    #     country = "Україна",
    #     price = "2",
    #     description = "Відвідуйте дуже гарні пляжі Криму за 2 гривні"
    # )
    # product1 = Tour(
    #     title = "Запоріжжя",
    #     date = "24.09.2025",
    #     country = "Україна",
    #     price = "4",
    #     description = "Відвідуйте Артема Московського"
    # )
    # product2 = Tour(
    #     title = "Москва",
    #     date = "Та хоть завтра",
    #     country = "россія",
    #     price = "-1",
    #     description = "Отримайте можливість набити пику одному карлику"
    # )
    tours_list = Tour.query.all()

    # DATABASE.session.add(product)
    # DATABASE.session.add(product1)    
    # DATABASE.session.add(product2)
    # DATABASE.session.commit()
    return flask.render_template(
        template_name_or_list = "tour.html", 
        tours_list = tours_list, 
        is_auth = current_user.is_authenticated,
        user_data = User.query.get(current_user.id) if current_user.is_authenticated else None
    )

def show_view_tour(id):
    tour = Tour.query.get(id)
    return flask.render_template(template_name_or_list = "tour_view.html", tour = tour)

    