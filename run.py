import requests, re, json
import card_page.constants as const
from card_page.card_page import Card_Page
from requests.exceptions import HTTPError

with Card_Page() as bot:
    bot.land_first_page()
