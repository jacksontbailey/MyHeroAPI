import json, re
import logging
import card_page.constants as const


def multi_list_comparator(all_urls, json_file_urls):
    # -- Converts both of my lists into a set in order to use symmetric difference to compare
    # -- the items in the list without worrying about their order. Then converts back to a list.
    urls_still_needed = list(set(all_urls).symmetric_difference(set(json_file_urls)))
    print(f"{urls_still_needed} \n ^^^These are urls still needed^^^")
    return urls_still_needed


def retrieve_json_items(filename):
    urls = []
    with open(filename, 'r') as data:
        json_dict = json.load(data)
    for card in json_dict:
        urls.append(card['card_tcg_url'])
    return urls

def check_for_missing_attributes(attribute):
    if len(attribute) == 0:
        print(f"Attribute - {attribute}: Equals None")
        attribute = "None"
    else:
        attribute = str(attribute[1])
    return(attribute)


def universal_card_info(bot, urls):
    temporary_card_list = []
    
    try:
        loop = 0
        for i, val in enumerate(urls):
            description = bot.open_all_card_urls(urls[i])
            print(val, description)

            #-- Find out if the card is a Character, Attack, Foundation, Action, or Asset
            tcg_url = val
            card_name = description[0]
            card_description_raw = description[1]
            card_rarity = check_for_missing_attributes(description[2][0])
            card_number_unparsed = check_for_missing_attributes(description[2][1])
            card_type = check_for_missing_attributes(description[2][2])
            card_resource_symbols_unparsed = check_for_missing_attributes(description[2][3])
            card_check = check_for_missing_attributes(description[2][4])
            card_difficulty = check_for_missing_attributes(description[2][5])
            card_block_modifier = check_for_missing_attributes(description[2][6])
            card_block_zone = check_for_missing_attributes(description[2][7])
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
            print(f"items printed: {loop}")
    
    except BaseException as err:
        print(f"\n\nUnexpected {err=}, {type(err)=} \n\nproblem card: {val, description}")

    finally:
        return(temporary_card_list)        



def attack_card_info(description):
    card_attack_speed = check_for_missing_attributes(description[2][8])
    card_attack_zone = check_for_missing_attributes(description[2][9])
    card_attack_damage = check_for_missing_attributes(description[2][10])
    card_keywords_unparsed = description[2][11]

    return(card_attack_speed, card_attack_zone, card_attack_damage, card_keywords_unparsed)

def character_card_info(description):
    card_vitality = check_for_missing_attributes(description[2][9])
    card_hand_size = check_for_missing_attributes(description[2][8])
    card_keywords_unparsed = description[2][10]

    return(card_hand_size, card_vitality, card_keywords_unparsed)


def other_shared_type_info(description):
    card_keywords_unparsed = description[2][8]
    return(card_keywords_unparsed)