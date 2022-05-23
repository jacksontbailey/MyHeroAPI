BASE_URL = "https://sitemap.tcgplayer.com/universus.0.xml"
TEST_URL = "https://www.tcgplayer.com/product/251196/universus-universus-my-hero-academia-capture-evil-doers"

WORK_DRIVER = r"C:\Users\jbailey\Selenium\chromedriver.exe"
HOME_FOLDER = r"C:\Program Files (x86)\chromedriver.exe"


JSON_FILE_URL = r"MHAcards.json"

# -- Regex Expressions
BASE_URL_REGEX = r"(product\/)\d+\/(universus-universus-my-hero-academia)((?!((\-.+)+)((booster-(box)|(pack))|pack|box|promo|judge)))((\-.+)+)((?<!\-xr)$)((?<!\-xsr)$)"
PARSE_JSON_REGEX = r"((https:\/\/)((.+)+)(?=<\/))"
CARD_NUMBER = r"(\/\d+)"
CARD_NAME = r"\(((XR)|(Judge)|(XSR)|(Regional (.+)+))\)"
DESCRIPTION_SPLIT = r"(\\)(\")"
UNICODE_SEARCH = r"[^\x00-\x7f]"
SPACE_DIGIT = r"((^ \d)|(^ \d ))"
SPACE_START_END = r"((^ )|( $))"
RELEASE_SET_PARSER = r"((: )(\w+|\s)+)$"
RELEASE_SET_STRING = r"(\w)(\w+|\s)+$"