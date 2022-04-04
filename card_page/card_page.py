from asyncio.windows_events import NULL
import imp, os, re
import card_page.constants as const
import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By



class Card_Page(webdriver.Chrome):
    def __init__(self, driver_path = r"C:\Users\jbailey\Selenium\chromedriver.exe", teardown=False):
        self.driver_path = driver_path
        self.chrome_service = Service(self.driver_path)
        self.teardown = teardown
        super(Card_Page, self).__init__(service=self.chrome_service)
        self.implicitly_wait(10)
        self.maximize_window()

    def __exit__(self, exec_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        driver = const.BASE_URL
        self.get(driver)
        self.implicitly_wait(10)
        print(driver)
        possible_direct_xpath = self.find_element_by_xpath("//span[starts-with(@id, 'folder0')]")
        print(possible_direct_xpath)
        

    
    def find_all_card_urls(self):
        possible_direct_xpath = self.find_element_by_xpath("/html/body/div[1]/urlset/url")
        
        print(possible_direct_xpath)

"""        for i in possible_direct_xpath:
            i = possible_direct_xpath.text()
            pattern = re.compile(const.BASE_URL_REGEX, re.IGNORECASE)
            if i == pattern:
                print(i)"""
"""        href = []
        card_urls = const.BASE_URL.find_elements_by_css_selector("span")
        print(card_urls)
        url_text = card_urls.text
        titled_columns =   {"Urls": NULL,
                            "Card Name": NULL, 
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
"""
                



#https://www.youtube.com/watch?v=j7VZsCCnptM