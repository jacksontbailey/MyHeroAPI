import requests, re, json, asyncio
import card_page.constants as const
from card_page.card_page import Card_Page
from requests.exceptions import HTTPError


def run_test():
    with Card_Page() as bot:
        get_all_urls = bot.land_first_page()
        description = bot.open_all_card_urls(get_all_urls[1])
        #for i in get_all_urls:
        #    asyncio.all_tasks

run_test()