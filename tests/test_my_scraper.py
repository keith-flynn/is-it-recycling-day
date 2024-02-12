import pytest
from my_scraper import Scraper

def test_connection():
    scraper = Scraper()
    assert scraper.page.status_code == 200
