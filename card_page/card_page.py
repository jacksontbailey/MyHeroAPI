import os
import card_page.constants as const
from selenium import webdriver



class Card_Page(webdriver.Chrome):
    def __init__(self, driver_path="C:/Program Files (x86)/chromedriver.exe"):
        self.driver_path = driver_path
        os.environ[PATH]+= self.driver_path
        super(Card_Page, self).__init__()

    def land_first_page(self):
        self.get(const.BASE_URL)

#https://www.youtube.com/watch?v=j7VZsCCnptM