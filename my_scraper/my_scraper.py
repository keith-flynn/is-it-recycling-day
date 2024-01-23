from bs4 import BeautifulSoup
import requests

class Scraper:
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