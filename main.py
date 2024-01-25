from my_scraper.my_scraper import Scraper
from database.sqlite_manager import DBManager
from email_sender.email_sender import EmailSender

# Connect and scrape
Scraper()

# Create an instance of EmailSender
email_sender = EmailSender()

# Database
db_manager = DBManager(email_sender)

# Check conditions for sending email
if conditions_met:
    email_sender = EmailSender()  # Create an instance of EmailSender
    email_sender.send_email("Recycling Alert", "Don't forget to put out the recycling tomorrow!")