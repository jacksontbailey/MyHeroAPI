from asyncio.windows_events import NULL
from cgitb import html
import imp, os, re, requests
import card_page.constants as const
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from requests.exceptions import HTTPError


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
        try:
            r = requests.get(const.BASE_URL)
            r.raise_for_status()
            json_response = r.text
            regex_1 = re.compile(const.PARSE_JSON_REGEX, re.MULTILINE|re.IGNORECASE)
            regex_2 = re.compile(const.BASE_URL_REGEX, re.IGNORECASE)

                
            extract_page_json = re.findall(regex_1, json_response)
            for card_url in extract_page_json:
                my_hero_url = re.search(regex_2, card_url[0])
                if my_hero_url:
                    print(card_url[0])
                #pattern = re.compile(const.BASE_URL_REGEX, re.IGNORECASE)
                #for url in pattern:
                #    print(url)

        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        

    
    def find_all_card_urls(self):
        possible_direct_xpath = self.find("/html/body/div[1]/urlset/url")
        
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