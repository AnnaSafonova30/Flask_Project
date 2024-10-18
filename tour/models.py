from main.settings import DATABASE


class Tour(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    title = DATABASE.Column(DATABASE.String(250), nullable = False)
    date = DATABASE.Column(DATABASE.String(250), nullable = False)
    country = DATABASE.Column(DATABASE.String(250), nullable = False)
    price = DATABASE.Column(DATABASE.Integer, nullable = False)
    description = DATABASE.Column(DATABASE.String(250), nullable = False)