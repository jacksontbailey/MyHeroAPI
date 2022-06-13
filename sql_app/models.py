from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Card(Base):
    __tablename__ = "cards"

    block_modifier = Column(Integer, index=True)
    block_zone = Column(String, index=True)
    check = Column(Integer, index=True)
    description = Column(String, index=True)
    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String, unique=True, index=True)
    keyword = Column(String)
    name = Column(String, index=True)
    play_difficulty = Column(Integer, index=True)
    rarity = Column(String, index=True)
    type = Column(String, index=True)

    sets = relationship("Set", back_populates="owner")
    symbols = relationship("Symbol", back_populates="owner")


class Set(Base):
    __tablename__ = "sets"

    set = Column(String, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("cards.id"))

    owner = relationship("Card", back_populates="sets")

class Symbol(Base):
    __tablename__ = "symbols"

    symbol = Column(String, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("cards.id"))

    owner = relationship("Card", back_populates="symbols")

class Character_Type(Base):
    __tablename__ = "character"

    id = Column(Integer, primary_key=True, index=True)
    max_health = Column(Integer, index=True)
    starting_hand_size = Column(Integer, index=True)
    type = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("cards.id"))

class Attack_Type(Base):
    __tablename__ = "attack"

    id = Column(Integer, primary_key=True, index=True)
    ability = Column(String, index=True)
    attack_keywords = Column(String, index=True)
    attack_zone = Column(String, index=True)
    damage = Column(Integer, index=True)
    speed = Column(Integer, index=True)
    type = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("cards.id"))

class Foundation_Type(Base):
    __tablename__ = "foundation"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("cards.id"))

class Action_Type(Base):
    __tablename__ = "action"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("cards.id"))

class Asset_Type(Base):
    __tablename__ = "asset"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("cards.id"))

