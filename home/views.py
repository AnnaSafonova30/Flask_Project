import flask
from flask_login import current_user
from user.models import User
from flask_mail import Message
from main.settings import mail

def show_home_list():
    if flask.request.method == "POST":
        client_name = flask.request.form.get('client_name')
        feedback = flask.request.form.get('feedback')
        email = flask.request.form.get('email')

        review = f"""
        name: {client_name}
        feedback: {feedback}
        email: {email}
        """
      
        message = Message(
            "Ваш відгук",
            sender="zx00xsanyazx@gmail.com", 
            recipients=['saschas1818@gmail.com'],  
            body=f"{review}"
        )

        mail.send(message)

    return flask.render_template(
        template_name_or_list = "home.html",
        is_auth = current_user.is_authenticated,
        user_data = User.query.get(current_user.id) if current_user.is_authenticated else None
    )

