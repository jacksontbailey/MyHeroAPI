import json
import database as db
from fastapi import APIRouter, HTTPException, Header, Path, Query, status
from card_page.card_classes import *
from fastapi.responses import JSONResponse



router = APIRouter()


from database import (
    fetch_all_cards,
    fetch_card_by_id,
    fetch_card_by_name,
    create_card,
    update_card,
    remove_card
)


with open(f"./{const.JSON_FILE_URL}") as f:
    card_database = json.load(f)
    u = Unicode_Parser()

    regular_cards = []
    provisional_cards = []
    full_card_results = []
    full_prov_card_results = []
    #my_middleware = LowerCaseMiddleware()
    #router.middleware("http")(my_middleware)


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
        new_card = Card(
                    block_modifier= c['card_block_modifier'],
                    block_zone=c['card_block_zone'],
                    check=c["card_check"],
                    description=c["card_description"],
                    id=c["card_release_number"],
                    image_url=c["card_image"],
                    name=c["card_name"],
                    play_difficulty=c['card_difficulty'],
                    rarity=c["card_rarity"],
                    set=c["set_name"],
                    symbols=c["card_resource_symbols"],
                )
        
        if ct == "Attack":
                new_card.type_attributes = {
                                "attack_keywords": c["card_keywords"],
                                "attack_zone": c['card_attack_zone'],
                                "damage": c["card_attack_damage"],
                                "speed": c["card_attack_speed"],
                                "type": ct
                                }

        elif ct == "Character":
            new_card.type_attributes = {
                                "max_health": c["card_vitality"],
                                "starting_hand_size": c["card_hand_size"],
                                "type": ct,
                                }

            new_card.keyword = c["card_keywords"]

        elif (ct == "Action") or (ct == "Asset") or (ct == "Foundation"):
                new_card.type_attributes = {"type": ct}
                new_card.keyword=c["card_keywords"]

        else:
            print("Card not in types")


        # -- Determines if the card is a provisional card or normal card (provisional cards are ones that are specially released for tournament participants but aren't in any set list)
        if cs == "Provisional Showdown":
            full_prov_card_results.append(new_card)

        else:
            full_card_results.append(new_card)


@router.get("", status_code=status.HTTP_200_OK)
async def api_introduction():
    return{"Guide": "Here are all of the different get requests you can make using this API."}


# -- Uses queries to find all cards within provided parameters
@router.get("/", status_code=status.HTTP_200_OK, tags=["All Cards"])
async def card_search(
        t: str | None = Query(
            default = None, 
            title = "Type", 
            description = "Query cards in database that have 'x' type. Types available: Attack, Asset, Action, Character, Foundation"
            ), 
        r: str | None =  Query(
            default = None, 
            title = "Rarity", 
            description = "Query cards in database that have 'x' rarity. Rarities available: Common, Uncommon, Rare, Ultra Rare, Starter Exclusive, Promo, Secret Rare"
            ), 
        sm: str  | None = Query(
            default = None, 
            title = "Symbol", 
            description = "Query cards in database that have 'x' symbol(s). Symbols available: Air, All, Chaos, Death, Earth, Evil, Fire, Good, Infinity, Life, Order, Void, Water"
            ),
        s: str | None = Header(
            default = None, 
            title = "Set", 
            description = "Query cards in database that are in 'x' set. Sets available: My Hero Academia, Crimson Rampage, Provisional Showdown"
            )):
    
    results = [] 

    for card in full_card_results:
        if t != None:
            if card.type_attributes["type"].upper() == t.upper():
                results.append(card)
        
        if r != None:            
            if card.rarity.upper() == r.upper():
                results.append(card)
        
        if sm != None:
            for symbol in card.symbols:
                if symbol.upper() == sm.upper():
                    results.append(card)

        if s != None:
            s = re.sub(" ","-", s)
            set = card.set
            set = re.sub(" ", "-", set)
            if set.upper() == s.upper():
                results.append(card)

    
    for card in full_prov_card_results:    
        if t != None:
            if card.type_attributes["type"].upper() == t.upper():
                results.append(card)
        
        if r != None:            
            if card.rarity.upper() == r.upper():
                results.append(card)
        
        if sm != None:
            for symbol in card.symbols:
                if symbol.upper() == sm.upper():
                    results.append(card)

        if s != None:
            s = re.sub(" ","-", s)
            set = card.set
            set = re.sub(" ", "-", set)
            if set.upper() == s.upper():
                results.append(card)
    return {"cards": sorted(results, key= lambda x:x.id)}


@router.get("/cards", status_code=status.HTTP_200_OK, tags=["Normal Cards"])
async def card_list():
    response = await fetch_all_cards()
    if response:
        return response
    raise HTTPException(
        status_code= status.HTTP_404_NOT_FOUND,
        detail="There is no card in our database with that name",
    )



# -- Searches for cards with the card Name or ID
@router.get("/cards/{id}", status_code=status.HTTP_200_OK, tags=["Normal Cards"], response_model=Card)
async def card_name(id: int | str):
    response = None

    if type(id) == int:
        response = await fetch_card_by_id(id)
    elif type(id) == str:
        card = id.replace("_", " ")
        response = await fetch_card_by_name(card)
    else:
        return("Invalid Type")

    if response:
        return response

    raise HTTPException(
        status_code= status.HTTP_404_NOT_FOUND,
        detail="There is no card in our database with that name",
    )