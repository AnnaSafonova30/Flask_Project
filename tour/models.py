from main.settings import database


class Tour(database.Model):
    id = database.Column(database.Integer, primary_key = True)
    title = database.Column(database.String(250), nullable = False)
    date = database.Column(database.String(250), nullable = False)
    country = database.Column(database.String(250), nullable = False)
    price = database.Column(database.Integer, nullable = False)
    description = database.Column(database.String(250), nullable = False)