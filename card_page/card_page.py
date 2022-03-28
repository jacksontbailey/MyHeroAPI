import os
import card_page.constants as const
from selenium import webdriver
from selenium.webdriver.chrome.service import Service



class Card_Page(webdriver.Chrome):
    def __init__(self):
        self.driver_path = "C:/Users/jbailey/Selenium/chromedriver.exe"
        os.environ['PATH'] += self.driver_path
        print(f"This is my path: {os.environ['PATH']}")
        super(Card_Page, self).__init__()

    def __exit__(self, exec_type, exc_val, exc_tb):
        self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

#https://www.youtube.com/watch?v=j7VZsCCnptM