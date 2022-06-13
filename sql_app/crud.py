from sqlalchemy.orm import Session

from . import models
import cards


def get_card(db: Session, card_id: int):
    return db.query(models.Card).filter(models.Card.id == card_id).first()

def get_cards(db: Session, skip: int = 0, limit: int = 20):
    return db.query(models.Card).offset(skip).limit(limit).all()

def create_card(db: Session, card: cards.CreateCard, set: models.Set, symbol: models.Symbol):
    db_card = models.Card(
        block_modifier = card.block_modifier, 
        block_zone = card.block_zone, 
        check = card.check, 
        description = card.description,
        id = card.id,
        image_url = card.image_url,
        keyword = card.keyword,
        name = card.name,
        play_difficulty = card.play_difficulty,
        rarity = card.rarity,
        set = models.Set(**set.dict(), owner_id = card.id),
        symbols = models.Symbol(**symbol.dict(), owner_id = card.id),
        type = card.type_attributes)
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card