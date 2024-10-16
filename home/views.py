from flask import *
from flask_mail import *
from main.settings import mail

def show_home_list():
    if request.method == "POST":
        client_name = request.form.get('client_name')
        feedback = request.form.get('feedback')
        email = request.form.get('email')

        review = f"""
        name: {client_name}
        feedback: {feedback}
        email: {email}
        """

        if email:
            sender_email = email
      
        message = Message(
            "Ваш відгук",
            sender=sender_email, 
            recipients=['saschas1818@gmail.com'],  
            body=f"{review}"
        )
         
        
       
        return "Повідомлення відправлено!"

    return render_template("home.html")


