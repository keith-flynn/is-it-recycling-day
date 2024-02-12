from bs4 import BeautifulSoup
import requests

class Scraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }
        self.url = 'https://daytonky.com/calendar-events/'
        self.page = self._get_page()

    def _get_page(self):
        return requests.get(self.url, headers=self.headers)

    def get_recycling_days(self):
        soup = BeautifulSoup(self.page.text, 'html.parser')
        recycling_days = [day for day in soup.find_all('dt', class_='mec-calendar-day') if day.find('a', string='Recycling Pick Up')]
        return recycling_days
