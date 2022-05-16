BASE_URL = "https://sitemap.tcgplayer.com/universus.0.xml"
TEST_URL = "https://www.tcgplayer.com/product/251196/universus-universus-my-hero-academia-capture-evil-doers"

# -- Regex Expressions
BASE_URL_REGEX = r"(product\/)\d+\/(universus-universus-my-hero-academia)((?!((\-.+)+)(booster-((box)|(pack))|pack|box)))((\-.+)+)((?<!\-xr)$)((?<!\-xsr)$)"
PARSE_JSON_REGEX = r"((https:\/\/)((.+)+)(?=<\/))"
CARD_NUMBER = r"(\/\d+)"
DESCRIPTION_SPLIT = r"(\\)(\")"
UNICODE_SEARCH = r"[^\x00-\x7f]"
SPACE_DIGIT = r"((^ \d)|(^ \d ))"
SPACE_START_END = r"((^ )|( $))"