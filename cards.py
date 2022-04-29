from enum import Enum
from typing import Optional
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
    type = "character"
    starting_hand_size: int
    max_health: int

class AttackCard(str, Enum):
    type = "character"
    zone = "Red" or "Orange" or "Yellow"
    speed: int
    damage: int
    keyword: list[AttackKeyword]
    ability: Optional[str]

class CardType(str, Enum):
    character = list[CharacterCard]
    attack = list[AttackCard]
    foundation = "foundation"
    action = "action"
    assets = "assets"

class Card(BaseModel):
    id: int
    image_url: str | None = None
    name: str
    type: CardType
    rarity: str
    play_difficulty: int
    block_modifier: int
    block_zone: str
    text_box: list[str]
    symbols: list[Symbol]
    check: int
    keyword: Optional[str] | None = None




