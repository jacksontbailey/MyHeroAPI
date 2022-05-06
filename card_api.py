from typing import Optional
from fastapi import FastAPI, Path, Query, status, Response
import cards, json
from cards import *
app = FastAPI()

with open("./MHAcards.json") as f:
    card_database = json.load(f)

    for val, card in enumerate(card_database):
        c = card_database[val]
        card_type = card.get("card_type")
        if card_type == "Attack":
            new_card = AttackCard(name=c["card_name"], 
                            id=c["card_number"],
                            rarity=c["card_rarity"],
                            play_difficulty=c['card_difficulty'],
                            block_modifier= c['card_block_modifier'],
                            block_zone=c['card_block_zone'],
                            text_box=c["card_description"],
                            symbols=c["card_resource_symbols"],
                            check=c["card_check"],
                            keyword=c["card_keywords"],
                            speed=c["card_attack_speed"],
                            damage=c["card_attack_damage"]
                            )
            print(new_card)
        elif card_type == "Asset":
            new_card = AssetCard(name=c["card_name"], 
                            id=c["card_number"],
                            rarity=c["card_rarity"],
                            play_difficulty=c['card_difficulty'],
                            block_modifier= c['card_block_modifier'],
                            block_zone=c['card_block_zone'],
                            text_box=c["card_description"],
                            symbols=c["card_resource_symbols"],
                            check=c["card_check"],
                            keyword=c["card_keywords"]
                            )
            print(new_card)
        elif card_type == "Action":
            new_card = ActionCard(name=c["card_name"], 
                            id=c["card_number"],
                            rarity=c["card_rarity"],
                            play_difficulty=c['card_difficulty'],
                            block_modifier= c['card_block_modifier'],
                            block_zone=c['card_block_zone'],
                            text_box=c["card_description"],
                            symbols=c["card_resource_symbols"],
                            check=c["card_check"],
                            keyword=c["card_keywords"]
                            )
            print(new_card)
        elif card_type == "Character":
            new_card = CharacterCard(name=c["card_name"], 
                            id=c["card_number"],
                            rarity=c["card_rarity"],
                            play_difficulty=c['card_difficulty'],
                            block_modifier= c['card_block_modifier'],
                            block_zone=c['card_block_zone'],
                            text_box=c["card_description"],
                            symbols=c["card_resource_symbols"],
                            check=c["card_check"],
                            keyword=c["card_keywords"],
                            starting_hand_size=c["card_hand_size"],
                            max_health=c["card_vitality"]
                            )
            print(new_card)
        elif card_type == "Foundation":
            new_card = FoundationCard(name=c["card_name"], 
                            id=c["card_number"],
                            rarity=c["card_rarity"],
                            play_difficulty=c['card_difficulty'],
                            block_modifier= c['card_block_modifier'],
                            block_zone=c['card_block_zone'],
                            text_box=c["card_description"],
                            symbols=c["card_resource_symbols"],
                            check=c["card_check"],
                            keyword=c["card_keywords"],
                            )
            print(new_card)
        else:
            print("Card not in types")

    


#@app.get("/")
#async def home():
#    return {"Greeting": "Welcome to the My Hero Academia Card Game API! This is a fan-made API that any developer is free to use. The only thing I ask is that you give me some credit when you use it, and/or buy me a coffee. This carbon-based lifeform needs Java installed..."}
#
#@app.get("/card-list")
#async def card_list():
#    return {"cards": []}
#
#@app.get("/get-card/{card_id}")
#def get_card(card_id: int = Path(None, description="The ID of the item you'd like to add.")):
#    return card_database[card_id]
#
#@app.get("/get-card-by-name")
#def get_card(name: str = Query(None, title = "Name", description="Name of item.")):
#    for card_id in card_database:
#        if card_database[card_id].name == name:
#            return card_database[card_id]
#    return {"Data": "Not found"}
#
#@app.get("/get-card-by-name/{card_id}")
#def get_card( *, card_id: int, name: Optional[str] = None, test: int):
#    for card_id in card_database:
#        if card_database[card_id].name == name:
#            return card_database[card_id]
#    return {"Data": "Not found"}
#
#
#@app.post("/add-card/{card_id}")
#def add_card(card_id: int, card: cards.Card):
#    if card_id in card_database:
#        return{"Error": "Card already exists in database."}
#    
#    card_database[card_id] = card
#    return card_database[card_id]
#
#@app.put("/update-card/{card_id}")
#def update_card(card_id: int, card: cards.UpdateCard):
#    if card_id not in card_database:
#        return{"Error": "Card does not exist in database."}
#    
#    if card.id != None:
#        card_database[card_id].id = card.id
#    
#    if card.image_url != None:
#        card_database[card_id].image_url = card.image_url
#    
#    if card.name != None:
#        card_database[card_id].name = card.name
#    
#    if card.type != None:
#        card_database[card_id].type = card.type
#    
#    if card.rarity != None:
#        card_database[card_id].rarity = card.rarity
#    
#    if card.play_difficulty != None:
#        card_database[card_id].play_difficulty = card.play_difficulty
#
#    if card.block_modifier != None:
#        card_database[card_id].block_modifier = card.block_modifier
#    
#    if card.block_zone != None:
#        card_database[card_id].block_zone = card.block_zone
#    
#    if card.text_box != None:
#        card_database[card_id].text_box = card.text_box
#    
#    if card.symbols != None:
#        card_database[card_id].symbols = card.symbols
#
#    if card.check != None:
#        card_database[card_id].check = card.check
#
#    if card.keyword != None:
#        card_database[card_id].keyword = card.keyword
#
#    return card_database[card_id]
#
#@app.delete("/delete-card")
#def delete_card(card_id: int = Query(..., description= "The ID of the card to delete must be greater than or equal to 0.", gt=0)):
#    if card_id not in card_database:
#        return {"Error": "ID does not exist."}
#    
#    del card_database[card_id]
#    return{"Success": "Item deleted"}
# / root with api explaination
# /card-names
# /cards-by-index/{index}
# /get-random-card
# /add-card
# /get-card-by-name?{}
# -- uvicorn card_api:app --reload