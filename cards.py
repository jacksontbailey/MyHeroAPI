from enum import Enum
from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel

class Symbol(str, Enum):
    air = "Air"
    all = "All"
    chaos = "Chaos"
    death = "Death"
    earth = "Earth"
    evil = "Evil"
    fire = "Fire"
    good = "Good"
    life = "Life"
    order = "Order"
    void = "Void"
    water = "Water"

class AttackKeyword(str, Enum):
    ally = "ally"
    breaker = "Breaker"
    charge = "Charge"
    combo = "Combo"
    ex = "EX"
    flash = "Flash"
    fury = "Fury"
    kick = "Kick"
    powerful = "Powerful"
    punch = "Punch"
    ranged = "Ranged"
    slam = "Slam"
    stun = "Stun"
    throw = "Throw"
    weapon = "Weapon"
    unique = "Unique"

class CharacterCard(str, Enum):
    starting_hand_size: int
    max_health: int
    version: str

class AttackCard(str, Enum):
    zone = "Red" or "Orange" or "Yellow"
    speed: int
    damage: int
    keyword: List[AttackKeyword]
    ability: Optional[dict[keyword[len(keyword)], str]]

class CardType(str, Enum):
    character = "character"
    attack = "attack"
    foundation = "foundation"
    action = "action"
    assets = "assets"

class Card(BaseModel):
    id: Optional[UUID] = uuid4
    image_url: str
    name: str
    play_difficulty: int
    block_total: int
    type: str
    text_box: str
    symbols: List[Symbol]
    check: int




