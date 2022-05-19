import re, json
from os import path
from fastapi import FastAPI

import card_page.constants as const
from reusable_functions import *
from card_page.data_collector import Card_Page

app = FastAPI()

def run_test():
    with Card_Page() as bot:
        get_all_urls = bot.land_first_page()
        print(get_all_urls)
    
        
        filename = const.JSON_FILE_URL
        loop = 0
        total_card_data = [] 
        print(filename)
        
        # Check if file exists
        if path.isfile(filename) is True:
            json_card_data = None
        
            with open(filename, "r+") as fp:
                print('started 1')
                json_card_data = json.load(fp)
                print("did 1")
                json_file_urls = retrieve_json_items(filename)
                needed_urls = multi_list_comparator(get_all_urls, json_file_urls)
        else:
            needed_urls = get_all_urls
            print("File hasn't been created yet")

                json_file_urls = retrieve_json_items(filename)
                needed_urls = multi_list_comparator(get_all_urls, json_file_urls)
            
            with open("MHAcards.json", "a+") as outfile:
                json.dump(json_card_data, outfile, indent=4)


        
                
            
        print(f"total card data = {total_card_data[0]}")
        json_card_data = total_card_data

        with open("MHAcards.json", "a+") as outfile:
            json.dump(json_card_data, outfile, indent=4)
                


run_test()
