import json, re
import card_page.constants as const


def multi_list_comparator(all_urls, json_file_urls):
    # -- Converts both of my lists into a set in order to use symmetric difference to compare
    # -- the items in the list without worrying about their order. Then converts back to a list.
    urls_still_needed = list(set(all_urls).symmetric_difference(set(json_file_urls)))
    print(f"HERE ARE ALL OF THE URLS STILL NEEDED: \n{urls_still_needed}")
    return urls_still_needed


def retrieve_json_items(filename):
    print('started 2')
    urls = []
    with open(filename, 'r') as data:
        json_dict = json.load(data)
    for card in json_dict:
        print(card['card_tcg_url'])
        urls.append(card['card_tcg_url'])
    return urls


def universal_card_info(bot, urls):
    loop = 0
    temporary_card_list = []

    for i, val in enumerate(urls):
        description = bot.open_all_card_urls(urls[i])
        print(val, description)
        # -- Loops through all of the card urls to get the data, but is currently set to max of 10 for testing purposes
        # -- Remove if/else statement to cycle through all of them.
        if loop < 3:
            #-- Find out if the card is a Character, Attack, Foundation, Action, or Asset
            tcg_url = val
            card_name = description[0]
            card_description_raw = description[1]
            card_rarity = description[2][0][1]
            card_number_unparsed = description[2][1][1]
            card_type = description[2][2][1]
            card_resource_symbols_unparsed = str(description[2][3][1])
            card_check = description[2][4][1]
            card_difficulty = description[2][5][1]
            card_block_modifier = description[2][6][1]
            card_block_zone = description[2][7][1]
            set_name = description[3]

            if len(card_description_raw) == 0:
                card_description = None
            else:
                card_description_unparsed = str(card_description_raw[0])
                card_description_unparsed = re.sub(const.DESCRIPTION_SPLIT, '', card_description_unparsed)
                card_description = card_description_unparsed.split("\n")

            card_number = re.sub(const.CARD_NUMBER, '', card_number_unparsed)
            card_resource_symbols = card_resource_symbols_unparsed.split(" ")
            card_set_name = re.search(const.RELEASE_SET_STRING, set_name, flags=re.IGNORECASE).group(0)

            card_details= {
                "card_name": card_name,
                "card_number": card_number,
                "card_tcg_url": tcg_url,
                "set_name": card_set_name,
                "card_type": card_type,
                "card_rarity": card_rarity,
                "card_description": card_description,
                "card_resource_symbols": card_resource_symbols,
                "card_check": card_check,
                "card_difficulty": card_difficulty,
                "card_block_modifier": card_block_modifier,
                "card_block_zone": card_block_zone,
            }

            if card_type == "Character":
                
                character_card_type = character_card_info(description)
                card_details['card_vitality'] = character_card_type[0]
                card_details['card_hand_size'] = character_card_type[1]
                card_details['card_keywords'] = character_card_type[2]

            elif card_type == "Attack":
                
                attack_card_type = attack_card_info(description)
                card_details['card_attack_speed'] = attack_card_type[0]
                card_details['card_attack_zone'] = attack_card_type[1]
                card_details['card_attack_damage'] = attack_card_type[2]
                card_details['card_keywords'] = attack_card_type[3]

            elif (card_type == "Foundation") | (card_type == "Action") | (card_type == "Asset"):
                
                other_card_type = other_shared_type_info(description)
                card_details['card_keywords'] = other_card_type[0]

            else:
                print("Card isn't of any type")
                None

            temporary_card_list.append(card_details)
            loop+=1
            print(f"{loop} loop total")
        else:
            print(f"loop equals {loop}")
            return(temporary_card_list)        



def attack_card_info(description):
    attack_speed_raw = description[2][8]
    attack_zone_raw = description[2][9]
    attack_damage_raw = description[2][10]
    card_keywords_unparsed = description[2][11]

    if len(attack_speed_raw) == 0:
        card_attack_speed = None
    else:
        card_attack_speed = str(attack_speed_raw[1])

    if len(attack_zone_raw) == 0:
        card_attack_zone = None
    else:
        card_attack_zone = str(attack_zone_raw[1])

    if len(attack_damage_raw) == 0:
        card_attack_damage = None
    else:
        card_attack_damage = str(attack_damage_raw[1])

    return(card_attack_speed, card_attack_zone, card_attack_damage, card_keywords_unparsed)

def character_card_info(description):
    card_vitality = description[2][9][1]
    card_hand_size = description[2][8][1]
    card_keywords_unparsed = description[2][10]

    return(card_hand_size, card_vitality, card_keywords_unparsed)


def other_shared_type_info(description):
    card_keywords_unparsed = description[2][8]
    return(card_keywords_unparsed)