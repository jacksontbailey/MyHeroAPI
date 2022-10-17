from card_page.card_classes import Card
from pymongo.collation import Collation

#MongoDB driver
from motor.motor_asyncio import AsyncIOMotorClient


client = AsyncIOMotorClient('mongodb://localhost:27017')
database = client.carddb
collection = database.card

# - Collation allows for case-insensitive lookups
colla = Collation(
                    locale = "en_US",
                    strength = 2,
                    numericOrdering = True,
                    backwards = False
                )

async def fetch_card_by_name(name):
    card = await collection.find_one({"name": name}).collation(colla)
    return card


async def fetch_card_by_id(id):
    card = await collection.find_one({"id": id})
    return card


async def fetch_all_cards():
    cards = []
    cursor = collection.find({})
    async for card in cursor:
        cards.append(Card(**card))
    
    return(len(cards), cards)


async def fetch_all_matches(queries, amount_limited):
    cards = []
    cursor = collection.find(queries).collation(colla).limit(amount_limited)
    async for card in cursor:
        cards.append(Card(**card))
    
    return(len(cards), cards)


async def create_card(card):
    document = card
    result = await collection.insert_one(document)
    return result


async def update_card(block_modifier, block_zone, check, description, 
                        id, image_url, keyword, name, play_difficulty, 
                        rarity, set, symbols, type_attributes
                    ):

    await collection.update_one({"name": name, "id": id},{"$set": {
        "block_modifier": block_modifier, "block_zone": block_zone,
        "check": check, "description": description, "image_url": image_url,
        "keyword": keyword, "play_difficulty": play_difficulty, "rarity": rarity,
        "set": set, "symbols": symbols, "type_attributes": type_attributes
    }})
    
    document = await collection.find_one({"name": name, "id": id})
    return document


async def remove_card(name):
    await collection.delete_one({"name": name})
    return True

