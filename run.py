import json
from os import path
from fastapi import FastAPI

import card_page.constants as const
from reusable_functions import *
from card_page.data_collector import Card_Page

app = FastAPI()

def run_test():
    with Card_Page() as bot:
        filename = const.JSON_FILE_URL
        get_all_urls = bot.land_first_page()
        
        # -- If JSON file exists, this will append the card data to the existing file.
        if path.isfile(filename) is True:
            with open(filename, "r+") as file:
                json_card_data = json.load(file)
                if type(json_card_data) is dict:
                    json_card_data = [json_card_data]

                json_file_urls = retrieve_json_items(filename)
                needed_urls = multi_list_comparator(get_all_urls, json_file_urls)
                retrieve_card_data = universal_card_info(needed_urls)
                
                for i in retrieve_card_data:
                    json_card_data.append(i)
                
                for card in json_card_data:
                    symbol = card['card_resource_symbols']
                    for i in symbol:
                        if i not in ["Air", "Good", "Chaos", "All", "Death", "Earth", "Evil", "Fire", "Life", "Order", "Void", "Water", "Infinity"]:
                            print(f"Card: {card['card_name']} ------ Symbols: {i}")
                    block_modifier = card['card_block_modifier']
                    for i in block_modifier:
                        if i.isdigit():
                            i = int(i)
                            json_card_data.append()
                            print(f"Card: {card['card_name']} ------ Value: {i}")
                with open(filename, "w+") as outfile:
                    json.dump(json_card_data, outfile, indent=4)

        # -- If JSON file doesn't exist, this will create a new one
        else:
            print("File hasn't been created yet")
            
            json_card_data = universal_card_info(get_all_urls)
            with open(filename, "w+") as outfile:
                json.dump(json_card_data, outfile, indent=4)                
        
        print("Finished retrieving card collection")


run_test()
