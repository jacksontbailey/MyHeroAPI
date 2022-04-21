import requests, re, json, asyncio
import card_page.constants as const
from card_page.card_page import Card_Page
from requests.exceptions import HTTPError


def run_test():
    with Card_Page() as bot:
        get_all_urls = bot.land_first_page()
        print(get_all_urls)
        print(type(get_all_urls))

        loop = 0
        for i, val in enumerate(get_all_urls):
            if loop < 10:
                description = bot.open_all_card_urls(get_all_urls[i])
                print(val, description)
                loop+=1
                print(f"{loop} loop total")
            else:
                print(f"loop equals {loop}")
                break
run_test()