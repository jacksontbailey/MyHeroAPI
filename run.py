import re, json

from fastapi import FastAPI
from cards import Card, CardType, AttackCard, AttackKeyword, CharacterCard, Symbol

import card_page.constants as const
from card_page.card_page import Card_Page
from requests.exceptions import HTTPError

app = FastAPI()

def run_test():
    with Card_Page() as bot:
        get_all_urls = bot.land_first_page()
        print(get_all_urls)
        print(type(get_all_urls))
    
    # -- Loops through all of the card urls to get the data, but is currently set to max of 10 for testing purposes
    # -- Remove if/else statement to cycle through all of them.

        json_card_data = [] 
        loop = 0
        for i, val in enumerate(get_all_urls):
            if loop < 20:
                description = bot.open_all_card_urls(get_all_urls[i])
                print(val, description)

    #-- Find out if the card is a Character, Attack, Foundation, Action, or Asset

                card_name = description[0]
                card_description_unparsed = str(description[1][0])
                card_rarity = description[2][0][1]
                card_number_unparsed = description[2][1][1]
                card_type = description[2][2][1]
                card_resource_symbols_unparsed = str(description[2][3][1])
                card_check = description[2][4][1]
                card_difficulty = description[2][5][1]
                card_block_modifier = description[2][6][1]
                card_block_zone = description[2][7][1]

                card_number = re.sub(const.CARD_NUMBER, '', card_number_unparsed)
                card_description_unparsed = re.sub(const.DESCRIPTION_SPLIT, '', card_description_unparsed)
                card_description = card_description_unparsed.split("\n")
                card_resource_symbols = card_resource_symbols_unparsed.split(" ")

                if card_type == "Character":
                    card_hand_size = description[2][8][1]
                    card_vitality = description[2][9][1]
                    card_keywords_unparsed = description[2][10]

                    card_details = {
                        "card_name": card_name,
                        "card_description": [card_description],
                        "card_rarity": card_rarity,
                        "card_number": card_number,
                        "card_type": card_type,
                        "card_resource_symbols": [card_resource_symbols],
                        "card_check": card_check,
                        "card_difficulty": card_difficulty,
                        "card_block_modifier": card_block_modifier,
                        "card_block_zone": card_block_zone,
                        "card_hand_size": card_hand_size,
                        "card_vitality": card_vitality,
                        "card_keywords_unparsed": card_keywords_unparsed,
                    }
                    card_copy = card_details.copy()
                    json_card_data.append(card_copy)
                    
                elif card_type == "Attack":
                    card_attack_speed = description[2][8][1]
                    card_attack_zone = description[2][9][1]
                    card_attack_damage = description[2][10][1]
                    card_keywords_unparsed = description[2][11]

                    card_details = {
                        "card_name": card_name,
                        "card_description": [card_description],
                        "card_rarity": card_rarity,
                        "card_number": card_number,
                        "card_type": card_type,
                        "card_resource_symbols": [card_resource_symbols],
                        "card_check": card_check,
                        "card_difficulty": card_difficulty,
                        "card_block_modifier": card_block_modifier,
                        "card_block_zone": card_block_zone,
                        "card_attack_speed": card_attack_speed,
                        "card_attack_zone": card_attack_zone,
                        "card_attack_damage": card_attack_damage,
                        "card_keywords_unparsed": card_keywords_unparsed
                    }

                    card_copy = card_details.copy()
                    json_card_data.append(card_copy)


                elif (card_type == "Foundation") | (card_type == "Action") | (card_type == "Asset"):
                    card_keywords_unparsed = description[2][8]

                    card_details = {
                        "card_name": card_name,
                        "card_description": [card_description],
                        "card_rarity": card_rarity,
                        "card_number": card_number,
                        "card_type": card_type,
                        "card_resource_symbols": [card_resource_symbols],
                        "card_check": card_check,
                        "card_difficulty": card_difficulty,
                        "card_block_modifier": card_block_modifier,
                        "card_block_zone": card_block_zone,
                        "card_keywords_unparsed": card_keywords_unparsed
                    }

                    card_copy = card_details.copy()
                    json_card_data.append(card_copy)

                else:
                    None

                with open("MHAcards.json", "w") as outfile:
                    json.dump(json_card_data, outfile)


                loop+=1
                print(f"{loop} loop total")
            else:
                print(f"loop equals {loop}")
                break


run_test()
