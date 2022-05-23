from typing import Optional
from fastapi import FastAPI, Path, Query, status, Response
import cards, json
from cards import *
app = FastAPI()

with open("./MHAcards.json") as f:
    card_database = json.load(f)
    u = Unicode_Parser()

    full_card_results = []

    for val, card in enumerate(card_database):
        c = card_database[val]
        ct = card.get("card_type")
        kw = card.get("card_keywords")
        print(kw)
        revised_keywords = u.parse_list(kw)

        #print(ct)

        # -- Parses cards by their types since each type has a different amount of 
        # -- attributes that it paseses in.  
        if ct == "Attack":
            new_card = Card(name=c["card_name"], 
                            id=c["card_number"],
                            set=c["set_name"],
                            type_attributes= {"type": ct,
                                "attack_zone": c['card_attack_zone'],
                                "speed": c["card_attack_speed"],
                                "attack_keywords": c["card_keywords"],
                                "damage": c["card_attack_damage"]
                            },
                            card_type=c["card_type"],
                            rarity=c["card_rarity"],
                            play_difficulty=c['card_difficulty'],
                            block_modifier= c['card_block_modifier'],
                            block_zone=c['card_block_zone'],
                            description=c["card_description"],
                            symbols=c["card_resource_symbols"],
                            check=c["card_check"],
                            )
            full_card_results.append(new_card)
            #print(full_card_results)

        elif ct == "Asset":
            new_card = Card(name=c["card_name"], 
                            id=c["card_number"],
                            set=c["set_name"],
                            type_attributes={"type": ct},
                            rarity=c["card_rarity"],
                            card_type=c["card_type"],
                            play_difficulty=c['card_difficulty'],
                            block_modifier= c['card_block_modifier'],
                            block_zone=c['card_block_zone'],
                            description=c["card_description"],
                            symbols=c["card_resource_symbols"],
                            check=c["card_check"],
                            keyword=c["card_keywords"]
                            )
            full_card_results.append(new_card)
            #print(full_card_results)


        elif ct == "Action":
            new_card = Card(name=c["card_name"], 
                            id=c["card_number"],
                            set=c["set_name"],
                            type_attributes= {"type": ct},
                            rarity=c["card_rarity"],
                            play_difficulty=c['card_difficulty'],
                            block_modifier= c['card_block_modifier'],
                            block_zone=c['card_block_zone'],
                            description=c["card_description"],
                            symbols= c["card_resource_symbols"],
                            check=c["card_check"],
                            keyword=c["card_keywords"]
                            )
            full_card_results.append(new_card)
            #print(full_card_results)

        elif ct == "Character":
            new_card = Card(name=c["card_name"], 
                            id=c["card_number"],
                            set=c["set_name"],
                            type_attributes= {
                                "type": ct,
                                "starting_hand_size": c["card_hand_size"],
                                "max_health": c["card_vitality"]
},
                            rarity=c["card_rarity"],
                            play_difficulty=c['card_difficulty'],
                            block_modifier= c['card_block_modifier'],
                            block_zone=c['card_block_zone'],
                            description=c["card_description"],
                            symbols=c["card_resource_symbols"],
                            check=c["card_check"],
                            keyword=c["card_keywords"],
                            )
            full_card_results.append(new_card)
            #print(full_card_results)

        elif ct == "Foundation":
            new_card = Card(name=c["card_name"], 
                            id=c["card_number"],
                            set=c["set_name"],
                            type_attributes= {"type": ct},
                            rarity=c["card_rarity"],
                            play_difficulty=c['card_difficulty'],
                            block_modifier= c['card_block_modifier'],
                            block_zone=c['card_block_zone'],
                            description=c["card_description"],
                            symbols=c["card_resource_symbols"],
                            check=c["card_check"],
                            keyword=c["card_keywords"],
                            )
            full_card_results.append(new_card)
            #print(full_card_results)

        else:
            print("Card not in types")

#print(full_card_results)
    


@app.get("/")
async def home():
    return {"Greeting": "Welcome to the My Hero Academia Card Game API! This is a fan-made API that any developer is free to use. The only thing I ask is that you give me some credit when you use it, and/or buy me a coffee. This carbon-based lifeform needs Java installed..."}

@app.get("/card-list")
async def card_list():
    return {"cards": full_card_results}

@app.get("/get-card/{card_id}")
def get_card(card_id: int = Path(None, description="The ID of the item you'd like to add.")):
    return full_card_results[card_id]

@app.get("/get-card-by-name")
def get_card(name: str = Query(None, title = "Name", description="Name of item.")):
    for card_id in full_card_results:
        if full_card_results[card_id].name == name:
            return full_card_results[card_id]
    return {"Data": "Not found"}

@app.get("/get-card-by-name/{card_id}")
def get_card( *, card_id: int, name: Optional[str] = None, test: int):
    for card_id in full_card_results:
        if full_card_results[card_id].name == name:
            return full_card_results[card_id]
    return {"Data": "Not found"}


@app.post("/add-card/{card_id}")
def add_card(card_id: int, card: cards.Card):
    if card_id in full_card_results:
        return{"Error": "Card already exists in database."}
    
    full_card_results[card_id] = card
    return full_card_results[card_id]

@app.put("/update-card/{card_id}")
def update_card(card_id: int, card: cards.UpdateCard):
    if card_id not in full_card_results:
        return{"Error": "Card does not exist in database."}
    
    if card.id != None:
        full_card_results[card_id].id = card.id

    if card.set != None:
        full_card_results[card_id].set = card.set
    
    if card.image_url != None:
        full_card_results[card_id].image_url = card.image_url
    
    if card.name != None:
        full_card_results[card_id].name = card.name
    
    if card.type != None:
        full_card_results[card_id].type = card.type
    
    if card.rarity != None:
        full_card_results[card_id].rarity = card.rarity
    
    if card.play_difficulty != None:
        full_card_results[card_id].play_difficulty = card.play_difficulty

    if card.block_modifier != None:
        full_card_results[card_id].block_modifier = card.block_modifier
    
    if card.block_zone != None:
        full_card_results[card_id].block_zone = card.block_zone
    
    if card.description != None:
        full_card_results[card_id].description = card.description
    
    if card.symbols != None:
        full_card_results[card_id].symbols = card.symbols

    if card.check != None:
        full_card_results[card_id].check = card.check

    if card.keyword != None:
        full_card_results[card_id].keyword = card.keyword

    return full_card_results[card_id]

@app.delete("/delete-card")
def delete_card(card_id: int = Query(..., description= "The ID of the card to delete must be greater than or equal to 0.", gt=0)):
    if card_id not in card_database:
        return {"Error": "ID does not exist."}
    
    del card_database[card_id]
    return{"Success": "Item deleted"}
# / root with api explaination
# /card-names
# /cards-by-index/{index}
# /get-random-card
# /add-card
# /get-card-by-name?{}
# -- uvicorn card_api:app --reload