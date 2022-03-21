import requests, re, asyncio, shutil
from cgitb import text
from pprint import pprint
from bs4 import BeautifulSoup

parent_url = "https://mhacardgame.com/cards/"
page = requests.get(parent_url).text

soup = BeautifulSoup(page, "html.parser")
imgs = soup.find_all('img')

async def download_card_images():
    for card in cards.values():
        pattern = re.compile(r'\d+(-([a-z])+)+(-\d).png$', re.IGNORECASE)
        file_name_search = pattern.search(card)
        file_name= file_name_search.group()
        res = requests.get(card, stream = True)
        if res.status_code == 200:
            with open(file_name, 'wb') as f:
                shutil.copyfileobj(res.raw, f)
            print(f'Image successfully Downloaded: {file_name}')
        else:
            print('Image couldn\'t be retrieved')
            
cards={}
i = 0

for img in (imgs):
    if img.has_attr(r'srcset'):
        card = (img['src'])
        cards[i] =card
        i+=1

download_card_images()

"""card_name = (cards[1])
print(card_name)
pattern = re.compile(r'\d+(-([a-z])+)+(-\d).png$', re.IGNORECASE)
mo = pattern.search(card_name)
print(f"Here is the pattern I found: {mo.group()}")"""