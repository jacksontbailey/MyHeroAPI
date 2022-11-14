from schemas.schema_card import Card
from core.config import settings
from fastapi import HTTPException, status

# - Collation allows for case-insensitive lookups


async def fetch_card_by_name(name):
    cards=[]
    match = settings.CARD_COLL.find({"name": name}).collation(settings.INSENSITIVE).limit(1)
    
    for card in match:
        cards.append(Card(**card))

    return cards[0]



async def fetch_card_by_id(id):
    card = settings.CARD_COLL.find_one({"id": id})
    return card



async def fetch_all_cards():
    cards = []
    cursor = settings.CARD_COLL.find({})
    for card in cursor:
        cards.append(Card(**card))
    
    return(len(cards), cards)


async def fetch_all_card_urls():
    cards=[]
    cursor = settings.CARD_COLL.find({}, {'name': 1, 'id': 1})
    for card in cursor:
        name = card['name']
        url = f"http://localhost:3000/v1/cards/{card['id']}"
        cards.append({"name": name, "url": url})
    
    return (len(cards), cards)
        
        



async def fetch_all_matches(queries, amount_limited):
    cards = []
    cursor = settings.CARD_COLL.find(queries).collation(settings.SENSITIVE).limit(amount_limited)
    for card in cursor:
        print(card)
        cards.append(Card(**card))
    
    return(len(cards), cards)



def fetch_all_images():
    image_urls = []
    cursor = settings.CARD_COLL.find({}, {'image_url': 1, 'name': 1})
    for url in cursor:
        image_urls.append(url)
    
    return(image_urls)



async def create_card(card):
    document = card
    db = settings.USER_COLL

    name_match = db.find({'name': card['name']}).collation(settings.SENSITIVE)
    id_match = db.find({'id': card['id']})
    name_record = next(name_match, None)
    id_record = next(id_match, None)

    if name_record and id_record: 
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Card name and ID found in database.")
    else:
        result = settings.CARD_COLL.insert_one(document)
        return result



async def update_card(block_modifier, block_zone, check, description, 
                        id, image_url, keyword, name, play_difficulty, 
                        rarity, set, symbols, type_attributes
                    ):

    settings.CARD_COLL.update_one({"_id": id},{"$set": {
        "block_modifier": block_modifier, "block_zone": block_zone,
        "check": check, "description": description, "image_url": image_url,
        "keyword": keyword, "play_difficulty": play_difficulty, "rarity": rarity,
        "set": set, "symbols": symbols, "type_attributes": type_attributes
    }})
    
    document = settings.CARD_COLL.find_one({"name": name, "id": id})
    return document


async def remove_card(id):
    await settings.CARD_COLL.delete_one({"_id": f"ObjectId('{id}')"})
    return True