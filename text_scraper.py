from logging import NullHandler
import re, requests, asyncio, selenium
import pandas as pd
from bs4 import BeautifulSoup as bs
from card_page.card_page import Card_Page


with Card_Page() as bot:
    bot.land_first_page()

ser = Service("C:/Program Files (x86)/chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

async def open_card_from_list():
    None


async def get_card_data():
    None

page2 = "https://www.tcgplayer.com/product/250623/universus-universus-my-hero-academia-quick-creation"
page = "https://www.tcgplayer.com/search/universus/universus-my-hero-academia?productLineName=universus&setName=universus-my-hero-academia&view=grid&page="
card_names = {}
i = 0
p = 0



for p in range(1,2):

    driver.get(f"{page2}{p}")
    driver.implicitly_wait(10)

    WebDriverWait(driver, 30).until(
        EC.all_of(
            (By.CLASS_NAME, 'product-details__name'),
            (By.CLASS_NAME, 'product__item-details__description'),
            (By.CLASS_NAME, "product__item-details__attributes")
        )
    )
    driver.close()
    


    cards = soup.find_all("div", class_="search-result")
    print(soup.body)
    print(req.status_code)

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
    
    sleep(10)

print(card_names)