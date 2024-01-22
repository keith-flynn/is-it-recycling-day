from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText

class EmailSender:
    def __init__(self):
        load_dotenv()
        self.sender_email = os.environ.get("GMAIL_USER")
        self.receiver_email = os.environ.get("GMAIL_RECEIVER")
        self.password = os.environ.get("GMAIL_PASSWORD")

    def send_email(self, subject, body):
        message = MIMEText(body)
        message["Subject"] = subject
        message["From"] = self.sender_email
        message["To"] = self.receiver_email

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, self.receiver_email, message.as_string())

# Example usage
if __name__ == "__main__":
    email_sender = EmailSender()
    email_sender.send_email("Recycling Alert", "Don't forget to put out the recycling tomorrow!")
