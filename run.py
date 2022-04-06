import requests, re, json
import card_page.constants as const
from card_page.card_page import Card_Page
from requests.exceptions import HTTPError

#with Card_Page() as bot:
 #   bot.land_first_page()
try:
    r = requests.get(const.TEST_URL)
    r.raise_for_status()
    json_response = r.text
    json_1 = re.compile(const.PARSE_JSON_REGEX, re.MULTILINE|re.IGNORECASE)
    json_2 = re.compile(const.BASE_URL_REGEX, re.IGNORECASE)

    print(json_response)

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')