from typing import Optional
from fastapi import FastAPI, Path, Query, status, Response
import json, cards
from cards import *
app = FastAPI()

with open(f"./{const.JSON_FILE_URL}") as f:
    card_database = json.load(f)
    u = Unicode_Parser()

    regular_cards = []
    provisional_cards = []
    full_card_results = []
    full_prov_card_results = []

    for val, card in enumerate(card_database):
        c = card_database[val]
        ct = card.get("card_type")
        cs = card.get("set_name")

        if cs == "Provisional Showdown":
            single_card_basic_info = AllCards(id=c["card_release_number"], name=c['card_name'], url=f"localhost:8000/v1/prov-cards/{c['card_release_number']}")
            provisional_cards.append(single_card_basic_info)
        else:
            single_card_basic_info = AllCards(id=c["card_release_number"], name=c['card_name'], url=f"localhost:8000/v1/cards/{c['card_release_number']}")
            regular_cards.append(single_card_basic_info)




        # -- Parses cards by their types since each type has a different amount of 
        # -- attributes that it paseses in.  
        if ct == "Attack":
            new_card = Card(name=c["card_name"], 
                            id=c["card_release_number"],
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
            if cs == "Provisional Showdown":
                full_prov_card_results.append(new_card)

            else:
                full_card_results.append(new_card)

        elif (ct == "Action") or (ct == "Asset") or (ct == "Foundation"):
            new_card = Card(name=c["card_name"], 
                            id=c["card_release_number"],
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
            if cs == "Provisional Showdown":
                full_prov_card_results.append(new_card)

            else:
                full_card_results.append(new_card)

        elif ct == "Character":
            new_card = Card(name=c["card_name"], 
                            id=c["card_release_number"],
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
            if cs == "Provisional Showdown":
                full_prov_card_results.append(new_card)

            else:
                full_card_results.append(new_card)

        else:
            print("Card not in types")

#print(full_card_results)
    


@app.get("/")
async def home():
    return {"Greeting": "Welcome to the My Hero Academia Card Game API! This is a fan-made API that any developer is free to use. The only thing I ask is that you give me some credit when you use it, and/or buy me a coffee. This carbon-based lifeform needs Java installed..."}

@app.get("/v1/cards")
async def card_list():
    return{"count": len(regular_cards), "card_list": sorted(regular_cards, key=lambda x: x.id)}

@app.get("/v1/cards/{card_id}")
async def get_card(card_id: int = Path(ge=0)):
    for card in full_card_results:
        if card.id == card_id:
            return card
    return{"Data": "Not found"}

@app.get("/v1/cards/{card_name}")
async def get_prov_card(card_name: str):
    for card in full_prov_card_results:
        regex_card = re.sub(" ", "_", card.name)
        print(regex_card)
        if regex_card.upper() == card_name.upper():
            return card
    return{"Data": "Not found"}


@app.get("/v1/prov-cards")
async def prov_card_list():
    return{"count": len(provisional_cards), "provisional_card_list": sorted(provisional_cards, key=lambda x: x.id)}

@app.get("/v1/prov-cards/{card_id}")
async def get_card(card_id: int = Path(ge=0)):
    for card in full_prov_card_results:
        if card.id == card_id:
            return card
    return{"Data": "Not found"}

@app.get("/v1/prov-cards/{card_name}")
async def get_prov_card(card_name: str):
    for card in full_prov_card_results:
        regex_card = re.sub(" ", "_", card.name)
        if regex_card.upper() == card_name.upper():
            return card
    return{"Data": "Not found"}





@app.get("/v1/cards/{card_name}")
async def get_card(name: str = Query(None, title = "Name", description="Name of item.")):
    for card_id in full_card_results:
        if card_id[card_id].name == name:
            return full_card_results[card_id]
    return {"Data": "Not found"}

@app.get("/v1/get-card-by-name/{card_id}")
async def get_card( *, card_id: int, name: Optional[str] = None, test: int):
    for card_id in full_card_results:
        if full_card_results[card_id].name == name:
            return full_card_results[card_id]
    return {"Data": "Not found"}
# / root with api explaination
# /card-names
# /cards-by-index/{index}

# -- uvicorn api_paths:app --reload