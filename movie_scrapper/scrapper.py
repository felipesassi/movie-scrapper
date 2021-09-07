import requests
from bs4 import BeautifulSoup


def get_url_data(url):
    return requests.get(url)


def get_beautiful_soup_data(page_data):
    return BeautifulSoup(page_data.text, "html.parser")

