import os
import smtplib 
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path
from dotenv import load_dotenv

PORT = 587
EMAIL_SERVER = "smtp.gmail.com"

#loading env variables

parent_directory = Path(__file__).resolve().parent
envfile = parent_directory / ".env"
load_dotenv(envfile)

sender_email = os.getenv("EMAIL")
sender_password = os.getenv("PASSWORD")




def send_email(subject, reciever_email, name, birthday_date, age):

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("Wasif", sender_email))
    msg["To"] = reciever_email
    msg["BCC"] = sender_email

    msg.set_content(
        f"""/
            Hi {name},
            I hope you are well.
            Happy Birthday on turning {age+1} years old today {birthday_date}.
            Best Regards
            Wasif Ullah
        """
    )

    msg.add_alternative(
        f"""
        <html>
        <body>
            <p>Hi {name},</p>
            <p>I hope you are well.</p>
            <p>Happy Birthday on turning {age+1} years old today {birthday_date}.</p>
            <p>Best regards</p>
            <p>Wasif Ullah</p>
        </body>
        </html>
        """,
            subtype="html",
    )

    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()
        server.login(sender_email,sender_password)
        server.sendmail(sender_email,reciever_email,msg.as_string())



