import sqlite3
from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime
from email_sender import EmailSender

# Headers to mimic a real user's request
# The website really didn't like me before adding this
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}

url = 'https://daytonky.com/calendar-events/'
page = requests.get(url, headers=headers)

# Test the connection
print(f"Response Status Code: {page.status_code}")

soup = BeautifulSoup(page.text, 'html.parser')

# Filter days with "Recycling Pick Up" tag
recycling_days = [day for day in soup.find_all('dt', class_='mec-calendar-day') if day.find('a', string='Recycling Pick Up')]

# DEBUG
# Print the filtered days
for day in recycling_days:
    print(day)

# Add data to Pandas dataframe
recycling_day_info = []

for day in recycling_days:
    day_text = day.text.strip()
    date_str = day['data-mec-cell']

    # Convert date string to datetime object
    date_obj = datetime.strptime(date_str, "%Y%m%d")

    link = day.find('a')['href']
    recycling_day_info.append({'Date': date_obj, 'Day': day_text, 'Link': link})

df = pd.DataFrame(recycling_day_info)
print(df)

# SQLite database file
db_file = 'recycling_schedule.db'

# Add data to SQLite database
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS recycling_schedule (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        day TEXT,
        date TEXT,
        link TEXT
    )
''')

# Insert data into the table
for index, row in df.iterrows():
    cursor.execute('''
        INSERT INTO recycling_schedule (day, date, link)
        VALUES (?, ?, ?)
    ''', (str(row['Date']), row['Day'], row['Link']))

# Commit changes and close the connection
conn.commit()
conn.close()

print("Data added to SQLite database.")

# Check conditions for sending email
if conditions_met:
    email_sender = EmailSender()  # Create an instance of EmailSender
    email_sender.send_email("Recycling Alert", "Don't forget to put out the recycling tomorrow!")