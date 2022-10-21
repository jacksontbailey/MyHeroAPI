from schemas.schema_card import Card
from pymongo.collation import Collation
from core.config import settings

# - Collation allows for case-insensitive lookups
colla = Collation(
                    locale = "en_US",
                    strength = 2,
                    numericOrdering = True,
                    backwards = False
                )

async def fetch_card_by_name(name):
    card = settings.CARD_COLL.find_one({"name": name}).collation(colla)
    return card


async def fetch_card_by_id(id):
    card = settings.CARD_COLL.find_one({"id": id})
    return card


async def fetch_all_cards():
    cards = []
    cursor = settings.CARD_COLL.find({})
    for card in cursor:
        cards.append(Card(**card))
    
    return(len(cards), cards)


async def fetch_all_matches(queries, amount_limited):
    cards = []
    cursor = settings.CARD_COLL.find(queries).collation(colla).limit(amount_limited)
    for card in cursor:
        cards.append(Card(**card))
    
    return(len(cards), cards)


async def create_card(card):
    document = card
    result = settings.CARD_COLL.insert_one(document)
    return result


async def update_card(block_modifier, block_zone, check, description, 
                        id, image_url, keyword, name, play_difficulty, 
                        rarity, set, symbols, type_attributes
                    ):

    settings.CARD_COLL.update_one({"name": name, "id": id},{"$set": {
        "block_modifier": block_modifier, "block_zone": block_zone,
        "check": check, "description": description, "image_url": image_url,
        "keyword": keyword, "play_difficulty": play_difficulty, "rarity": rarity,
        "set": set, "symbols": symbols, "type_attributes": type_attributes
    }})
    
    document = settings.CARD_COLL.find_one({"name": name, "id": id})
    return document


async def remove_card(name):
    await settings.CARD_COLL.delete_one({"name": name})
    return True

