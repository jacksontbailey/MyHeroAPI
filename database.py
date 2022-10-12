from card_page.card_classes import Card

#MongoDB driver
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
database = client.carddb
collection = database.card

async def fetch_card_by_name(name):
    # - Inline regex allows for case-insensitive lookup of card name
    card = await collection.find_one({"name": {"$regex": name, "$options": 'i'}})
    return card


async def fetch_card_by_id(id):
    card = await collection.find_one({"id": id})
    return card


async def fetch_all_cards():
    cards = []
    cursor = collection.find({})
    async for document in cursor:
        cards.append(Card(**document))
    
    return cards


async def create_card(card):
    document = card
    result = await collection.insert_one(document)
    return result


async def update_card(block_modifier, block_zone, check, description, 
                        id, image_url, keyword, name, play_difficulty, 
                        rarity, set, symbols, type_attributes
                    ):

    await collection.update_one({"name":name, "id": id},{"$set": {
        "block_modifier": block_modifier, "block_zone": block_zone,
        "check": check, "description": description, "image_url": image_url,
        "keyword": keyword, "play_difficulty": play_difficulty, "rarity": rarity,
        "set": set, "symbols": symbols, "type_attributes": type_attributes
    }})
    
    document = await collection.find_one({"name":name, "id": id})
    return document


async def remove_card(name):
    await collection.delete_one({"name": name})
    return True

