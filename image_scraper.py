import requests, re
from cgitb import text
from pprint import pprint
from bs4 import BeautifulSoup

parent_url = "https://mhacardgame.com/cards/"
page = requests.get(parent_url).text

soup = BeautifulSoup(page, "html.parser")
imgs = soup.find_all('img')

cards={}
i = 0
for img in (imgs):
    if img.has_attr(r'srcset'):
        card = (img['src'])
        cards[i] =card
        i+=1
pprint(cards)

print(cards[3])
