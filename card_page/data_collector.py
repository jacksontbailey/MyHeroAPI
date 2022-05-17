from asyncio.windows_events import NULL
from cgitb import html
import imp, os, re, requests,time
from operator import indexOf
import card_page.constants as const
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from requests.exceptions import HTTPError


class Card_Page(webdriver.Chrome):
    def __init__(self, driver_path = const.WORK_DRIVER, teardown=False):
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
        options.add_argument("start-maximized")
        options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])
        options.add_experimental_option('useAutomationExtension', False)

        pattern = self #replace with real regex pattern
        driver = webdriver.Chrome(const.WORK_DRIVER, options=options)
        driver.get(url)
        
        try:
            # -- Starts waiting process for parent elements of stuff I'm looking for on the page 
            wait = WebDriverWait(driver, 10)

            desc_el = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product__item-details__content")))
            attr_el = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product__item-details__attributes")))
            title_el = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-details__header")))
            

            # -- Needed to click dropdown button in order to retrieve all of the attributes for the card
            while True:
                try:
                    read_button = WebDriverWait(driver, .5).until(EC.presence_of_element_located((By.CLASS_NAME, "product__item-details__toggle")))
                    read_button.click()
                    break
                except:
                    print("No Drop Down button available")
                    break


            stats = []
            card_description_text = []

            # -- Gets the card title
            title = title_el.find_element(By.TAG_NAME, "h1")
            card_title = title.text

            # -- Gets the set name
            set = title_el.find_element(By.TAG_NAME, "h2")
            set_title = set.text

            # -- Gets the card description
            card_description = desc_el.find_elements(By.CLASS_NAME, "product__item-details__description")
            for card in card_description:
                card_description_text.append(card.text)

            # -- Gets all of the card stats besides the description
            items = attr_el.find_elements(By.TAG_NAME, value='li')
            
            for i in range(len(items)):
                val = items[i]
                card_stats = val.text
                card_stats_split = card_stats.split(":")
                stats.append(card_stats_split)
            return(card_title, card_description_text, stats, set_title)
            
        except:
            driver.quit()

                

#https://www.youtube.com/watch?v=j7VZsCCnptM