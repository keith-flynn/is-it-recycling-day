import sqlite3
import pandas as pd
from datetime import datetime
from email_sender.email_sender import EmailSender

class DBManager:
    def __init__(self, email_sender):
        # Receive an instance of EmailSender
        self.email_sender = email_sender

    def add_data_to_database(self):
        # Add data to Pandas dataframe
        recycling_day_info = []

        for day in EmailSender.recycling_days:
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

# Example usage
if __name__ == "__main__":
    # Create an instance of EmailSender
    email_sender = EmailSender()

    # Create an instance of DBManager and pass the EmailSender instance
    db_manager = DBManager(email_sender)
    db_manager.add_data_to_database()