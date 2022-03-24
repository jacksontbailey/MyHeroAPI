from logging import NullHandler
import re, requests, asyncio
import pandas as pd
from bs4 import BeautifulSoup as bs
from random import randint
from time import sleep 


async def open_card_from_list():
    None


async def get_card_data():
    None


page = "https://www.tcgplayer.com/search/universus/universus-my-hero-academia?productLineName=universus&setName=universus-my-hero-academia&view=grid&page="
card_names = {}
i = 0
p = 0



for p in range(1,2):

    req = requests.get(f"{page}{p}")
    soup = bs(req.text, "html.parser")

    cards = soup.find_all("div", class_="search-result")
    print(len(cards))

    for card in cards:
        title = soup.find("span", class_="search-result__title")
        url = soup.find("a", class_=f"search-result__image--{i}")
        unwanted_cards_pattern = re.compile(r'(\((.)+\)(\s?)$)|((Booster Box)(.+)+\[(.+)+\](\s?)$)', re.IGNORECASE)
        print(title.string)
        print(url.string)

        if unwanted_cards_pattern in title:
            print("regex in title")
            continue
        else:
            print(f"{title}: {url}")
            card_names[title] = url

        if i < 24:
            i+=1
        else:
            i = 0
            p+=1
    
    sleep(randint(2,7))

print(card_names)