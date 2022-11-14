from fastapi import APIRouter, status, HTTPException
from schemas.schema_card import Card, UpdateCard
from db.database import create_card, fetch_card_by_id, remove_card
from db.repository.users import remove_user

router = APIRouter()


@router.post("/add", status_code=status.HTTP_201_CREATED)
async def add_card(card: Card):
    response = await create_card(card.dict())
    if response:
        return response
    raise HTTPException(
        status_code= status.HTTP_409_CONFLICT,
        detail="There was an issue when adding the card to the database.",
    )
 

#@router.put("/update/{card_id}", response_model=Card)
#async def update_card(card_id: str, card: Card):
#    stored_card_data = await fetch_card_by_id(card_id)
#    mutable_card = dict(stored_card_data.pop("_id"))
#    stored_card_model = Card(**mutable_card)
#    update_data = card.dict(exclude_unset=True)
#    update_card = stored_card_model.copy(update=update_data)
    

@router.delete("/delete/{card_id}", status_code=status.HTTP_202_ACCEPTED)
async def delete_card(card_id: str):
    response = await remove_card(card_id)
    if response:
        return response
    raise HTTPException(
        status_code= status.HTTP_409_CONFLICT,
        detail=f"There was an issue when deleting the card {card_id} in the database.",
    )

@router.delete("/delete/{user_id}", status_code=status.HTTP_202_ACCEPTED)
async def delete_card(user_id: str):
    response = await remove_user(user_id)
    if response:
        return response
    raise HTTPException(
        status_code= status.HTTP_409_CONFLICT,
        detail=f"There was an issue when deleting the user {user_id} in the database.",
    )