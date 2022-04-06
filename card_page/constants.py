BASE_URL = "https://sitemap.tcgplayer.com/universus.0.xml"
BASE_URL_REGEX = r"(product\/)\d+\/(universus-universus-my-hero-academia)((?!((\-.+)+)(booster-((box)|(pack))|pack)))((\-.+)+)((?<!\-xr)$)((?<!\-xsr)$)"
PARSE_JSON_REGEX = r"((https:\/\/)((.+)+)(?=<\/))"