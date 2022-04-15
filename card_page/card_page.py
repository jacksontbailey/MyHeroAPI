from asyncio.windows_events import NULL
from cgitb import html
import imp, os, re, requests,time
import card_page.constants as const
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from requests.exceptions import HTTPError


class Card_Page(webdriver.Chrome):
    def __init__(self, driver_path = r"C:\Users\jbailey\Selenium\chromedriver.exe", teardown=False):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver_path = driver_path
        self.chrome_service = Service(self.driver_path)
        self.teardown = teardown
        super(Card_Page, self).__init__(service=self.chrome_service, options=options)
        self.implicitly_wait(10)
        self.maximize_window()

    def __exit__(self, exec_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        try:
            r = requests.get(const.BASE_URL)
            r.raise_for_status()
            json_response = r.text
            regex_1 = re.compile(const.PARSE_JSON_REGEX, re.MULTILINE|re.IGNORECASE)
            regex_2 = re.compile(const.BASE_URL_REGEX, re.IGNORECASE)
            all_urls = []

                
            extract_page_json = re.findall(regex_1, json_response)
            for card_url in extract_page_json:
                my_hero_url = re.search(regex_2, card_url[0])
                if my_hero_url:
                    all_urls.append(card_url[0])

            return all_urls        

        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        

    
    def open_all_card_urls(self, url):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        pattern = self #replace with real regex pattern
        driver = webdriver.Chrome(r"C:\Users\jbailey\Selenium\chromedriver.exe", options=options)
        driver.get(url)
        assert "My Hero Academia" in driver.title
        
        # -- Get card description for each card -- Need to still parse strong text from span
        card_description = driver.find_elements_by_class_name("product__item-details__description")
        for card in card_description:
            print(card.text)

        assert "No results found." not in driver.page_source
        
        url_text = driver.text
        titled_columns =   {"Urls": NULL,
                            "Card Name": driver.find_element_by_class_name("product-details__name").text, 
                            "Card ID": NULL, 
                            "Play Difficulty": NULL, 
                            "Block Total": NULL, 
                            "Type": NULL, 
                            "Text Box": NULL, 
                            "Symbols": NULL, 
                            "Check": NULL}
        url_db = pd.DataFrame(titled_columns)
        for url in url_text:
            if pattern.__str__ in url:
                href.append(url)
                print(url)
        url_db['url'] = href
        url_db.to_csv("cards.csv", sep="\t")
        print(url_db)
                

#https://www.youtube.com/watch?v=j7VZsCCnptM