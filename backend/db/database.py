from schemas.card_classes import Card
from pymongo.collation import Collation
from db.session import card_coll


# - Collation allows for case-insensitive lookups
colla = Collation(
                    locale = "en_US",
                    strength = 2,
                    numericOrdering = True,
                    backwards = False
                )

async def fetch_card_by_name(name):
    card = await card_coll.find_one({"name": name}).collation(colla)
    return card


async def fetch_card_by_id(id):
    card = await card_coll.find_one({"id": id})
    return card


async def fetch_all_cards():
    cards = []
    cursor = card_coll.find({})
    async for card in cursor:
        cards.append(Card(**card))
    
    return(len(cards), cards)


async def fetch_all_matches(queries, amount_limited):
    cards = []
    cursor = card_coll.find(queries).collation(colla).limit(amount_limited)
    async for card in cursor:
        cards.append(Card(**card))
    
    return(len(cards), cards)


async def create_card(card):
    document = card
    result = await card_coll.insert_one(document)
    return result


async def update_card(block_modifier, block_zone, check, description, 
                        id, image_url, keyword, name, play_difficulty, 
                        rarity, set, symbols, type_attributes
                    ):

    await card_coll.update_one({"name": name, "id": id},{"$set": {
        "block_modifier": block_modifier, "block_zone": block_zone,
        "check": check, "description": description, "image_url": image_url,
        "keyword": keyword, "play_difficulty": play_difficulty, "rarity": rarity,
        "set": set, "symbols": symbols, "type_attributes": type_attributes
    }})
    
    document = await card_coll.find_one({"name": name, "id": id})
    return document


async def remove_card(name):
    await card_coll.delete_one({"name": name})
    return True

