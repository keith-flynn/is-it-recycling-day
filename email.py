from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText

# Load environment variables from .env
load_dotenv()

def send_email(subject, body):
    sender_email = os.environ.get("GMAIL_USER")
    receiver_email = os.environ.get("GMAIL_RECEIVER")
    password = os.environ.get("GMAIL_PASSWORD")

    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

# Example usage
send_email("Recycling Alert", "Don't forget to put out the recycling tomorrow!")
