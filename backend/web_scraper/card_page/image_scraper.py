import requests, re, asyncio, shutil, os
from bs4 import BeautifulSoup

parent_url = "https://mhacardgame.com/cards/"
page = requests.get(parent_url).text

soup = BeautifulSoup(page, "html.parser")
imgs = soup.find_all('img')

def download_card_images():
    os.chdir("C:/Users/jbailey/OneDrive - OTO Development, LLC/Pictures/MHA images")

    for card in cards.values():
        pattern = re.compile(r'\d+((\-([a-z])+)+|(\-([\s\S]+)+))(.png$)', re.IGNORECASE)
        file_name_search = pattern.search(card)
        file_name= file_name_search.group()
        print(f"Here is the pattern I found: {file_name}")
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
        cards[i] = card
        print(f"This is a card: {cards[i]}")
        i+=1
