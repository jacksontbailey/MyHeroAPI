import re

from sqlalchemy import desc
import card_page.constants as const
from card_page.card_page import Card_Page
from requests.exceptions import HTTPError


def run_test():
    with Card_Page() as bot:
        get_all_urls = bot.land_first_page()
        print(get_all_urls)
        print(type(get_all_urls))
    
    # -- Loops through all of the card urls to get the data, but is currently set to max of 10 for testing purposes
    # -- Remove if/else statement to cycle through all of them. 
        loop = 0
        for i, val in enumerate(get_all_urls):
            if loop < 20:
                description = bot.open_all_card_urls(get_all_urls[i])
                print(val, description)

    #-- Find out if the card is a Character, Attack, Foundation, Action, or Asset

                card_name = description[0]
                card_description_unparsed = description[1]
                card_rarity = description[2][0][1]
                card_number = description[2][1][1]
                card_type = description[2][2][1]
                card_resource_symbols_unparsed = description[2][3][1]
                card_check = description[2][4][1]
                card_difficulty = description[2][5][1]
                card_block_modifier = description[2][6][1]
                card_block_zone = description[2][7][1]

                if card_type == "Character":
                    card_hand_size = description[2][8][1]
                    card_vitality = description[2][9][1]
                    card_keywords_unparsed = description[2][10]
                elif card_type == "Attack":
                    card_attack_speed = description[2][8][1]
                    card_attack_zone = description[2][9][1]
                    card_attack_damage = description[2][10][1]
                    card_keywords_unparsed = description[2][11]

                elif card_type == "Foundation":
                    card_keywords_unparsed = description[2][8]
                elif card_type == "Action":
                    card_keywords_unparsed = description[2][8]
                elif card_type== "Asset":
                    card_keywords_unparsed = description[2][8]
                else:
                    None

                card_number = re.sub(const.CARD_NUMBER, '', card_number)
                
                print(card_number)
                print(card_type)
                loop+=1
                print(f"{loop} loop total")
            else:
                print(f"loop equals {loop}")
                break
run_test()