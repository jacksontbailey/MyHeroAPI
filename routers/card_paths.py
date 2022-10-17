import json
import database

from fastapi import APIRouter, HTTPException, Header, Query, status
from card_page.card_classes import *



router = APIRouter()


from database import (
    fetch_all_cards,
    fetch_all_matches,
    fetch_card_by_id,
    fetch_card_by_name,
    create_card,
    update_card,
    remove_card
)


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
        sm: str | None = Query(
            default = None, 
            title = "Symbol", 
            description = "Query cards in database that have 'x' symbol(s). Symbols available: Air, All, Chaos, Death, Earth, Evil, Fire, Good, Infinity, Life, Order, Void, Water"
            ),
        s: str | None = Header(
            default = None, 
            title = "Set", 
            description = "Query cards in database that are in 'x' set. Sets available: My Hero Academia, Crimson Rampage, Provisional Showdown"
            ),
        limit: int = Header(
            default = 10,
            title = "Limit",
            description = "Amount of cards you get back from each search"
            )
        ):
    
    
    search_queries = {}
    if t != None:
        t_items = t.split(", ")
        key= 'type_attributes.type'
        value = {'$in': t_items}
        search_queries[key] = value
    
    if r != None:
        r_items = r.split(", ")
        key = 'rarity'
        value = {'$in': r_items}
        search_queries[key] = value
    
    if sm != None:
        sm_items = sm.split(", ")
        key = 'symbols'
        value = {'$in': sm_items}
        search_queries[key] = value

    if s != None:
        s_items = s.split(", ")
        key = 'set'
        value = {'$in': s_items}
        search_queries[key] = value
          
    
    results = None
    if len(search_queries)>0:
        results = await fetch_all_matches(queries=search_queries, amount_limited=limit)
    else:
        print("No search queries were provided.")
    
    
    if results:
        return({'count': results[0], 'cards': results[1]})
    raise HTTPException(
        status_code= status.HTTP_404_NOT_FOUND,
        detail="There is no card in our database with that name",
    )


@router.get("/cards", status_code=status.HTTP_200_OK, tags=["Normal Cards"])
async def card_list():
    response = await fetch_all_cards()
    if response:
        return({'count': response[0], 'cards': response[1]})
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