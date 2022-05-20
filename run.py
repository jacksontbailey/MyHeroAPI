import re, json
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
        print(get_all_urls)

        
        # -- If JSON file exists, this will append the card data to the existing file.
        if path.isfile(filename) is True:        
            with open(filename, "r+") as file:
                json_card_data = json.load(file)
                if type(json_card_data) is dict:
                    json_card_data = [json_card_data]

                json_file_urls = retrieve_json_items(filename)
                needed_urls = multi_list_comparator(get_all_urls, json_file_urls)
                retrieve_card_data = universal_card_info(bot, needed_urls)

                for i in retrieve_card_data:
                    json_card_data.append(i)
                
                with open(filename, "w+") as outfile:
                    json.dump(json_card_data, outfile, indent=4)

        # -- If JSON file doesn't exist, this will create a new one
        else:
            print("File hasn't been created yet")
            
            json_card_data = universal_card_info(bot, get_all_urls)
            with open(filename, "w+") as outfile:
                json.dump(json_card_data, outfile, indent=4)                


run_test()
