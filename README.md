# is-it-recycling-day
Scrape my town's website and send myself a reminder to take the can to the curb.

## About
A particularly erratic holiday season has left me with many questions. The most elusive of them all; *__Is it recycling day today?__*

The plan so far:
  - **Script for Web Scraping:** Write a Python script that uses Beautiful Soup and Requests to scrape the garbage and recycling days from the city's website. Extract the relevant information and save it to your chosen storage (SQLite database or CSV file).
  - **Task Scheduling with Cron:** Set up a Cron job to run your Python script at the desired frequency (e.g., weekly or monthly).
  - **Notification Script:** Write another Python script to read the stored information (from the database or CSV file) and send you an email notification using the smtplib module.

## To Run
  - Create the virtual environment
    - `python -m venv .venv` 
    - (This creates a virtual environment named ".venv")
    - Linux and OS X users may need to substitute `python3` in lieu of `python` in the CLI

  - Activate the virtual environment that was just created
    - `.venv\Scripts\activate` (Windows)
    - `source .venv/bin/activate`(Linux/OSX)

  - Set up requirements.txt (DEBUG)
    - pip install requests
    - pip install beautifulsoup4
    - pip install pandas

## Cron Setup Instructions
  - In your terminal, type the following command to open the crontab file for editing:
    - `crontab -e`
    - If this is the first time you're using cron, you may be prompted to choose an editor. Select your preferred editor (e.g., nano, vim, etc.)
  - Add your new cron job:
    - Each line in the crontab file represents a cron job. The syntax is as follows:
      - `[minute] [hour] [day] [month] [day_of_week] [command_to_be_executed]`
    - For example, the following line runs a script every day at 2:30 PM:
      - `30 14 * * * /path/to/your/script.py`
  - Save and exit
  - Verify your cron jobs:
    - List your current cron jobs: `crontab -l`
  - Enjoy!

## On the Topic of Waste Removal
The holiday season and freezing temperatures are enormous obstacles that our waste removal service workers navigate with relatively amazing levels of success. Even without those obstacles, waste removal on a scale necessary for modern society is nothing short of a marvel. This project is a learning experience and in no way a critique those services.

## License
[GNU GENERAL PUBLIC LICENSE](LICENSE)