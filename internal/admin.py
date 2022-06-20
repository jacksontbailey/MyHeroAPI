from fastapi import APIRouter

router = APIRouter()


#@router.post("/cards", status_code=status.HTTP_201_CREATED, tags=["Normal Cards"])
#async def create_card(card: Card):
#    c = cards.put(card.dict())
#    return c

# -- Creates new provisional cards
#@router.post("/prov-cards", status_code=status.HTTP_201_CREATED, tags=["Tournament Prize Cards"])
#async def create_prov_card(card: Card):
#    c = prov_cards.put(card.dict())
#    return c
