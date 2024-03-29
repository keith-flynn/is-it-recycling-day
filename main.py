from datetime import datetime, timedelta
from my_scraper.my_scraper import Scraper
from database.sqlite_manager import DBManager
from email_sender.email_sender import EmailSender

# Connect and scrape
Scraper()

# Create an instance of EmailSender
email_sender = EmailSender()

# Database
db_manager = DBManager(email_sender)

# Get today's date
today = datetime.now().date()

# Get the date for the next day
next_day = today + timedelta(days=1)

# Query the database to check if there's a recycling day for the next day
if db_manager.is_recycling_day(next_day):
    email_sender.send_email("Recycling Alert", "Don't forget to put out the recycling tomorrow!")