import re

from numpy import append
import card_page.constants as const
from enum import Enum
from typing import Annotated, Dict, Optional, Literal, Union
from pydantic import BaseModel, Field, ValidationError, validator


class Zone(str, Enum):
    high = "High"
    mid = "Mid"
    low = "Low"
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
    ally = "Ally"
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

class CharacterCard(BaseModel):
    type: Literal['Character']
    starting_hand_size: int
    max_health: int

class AttackCard(BaseModel):
    type: Literal['Attack']
    attack_zone: Zone
    speed: int
    damage: int
    attack_keywords: list[AttackKeyword]
    ability: Optional[str]

class FoundationCard(BaseModel):
    type: Literal['Foundation']
class ActionCard(BaseModel):
    type: Literal['Action']
class AssetCard(BaseModel):
    type: Literal['Asset']

class Card(BaseModel):
    name: str
    id: int
    type_attributes: Annotated[Union[CharacterCard, AttackCard, AssetCard, ActionCard,FoundationCard], Field(discriminator='type')]
    rarity: str
    image_url: str | None = None
    play_difficulty: int
    block_modifier: int
    block_zone: str
    description: list[str]
    symbols: list[Symbol]
    check: int
    keyword: Optional[list] | None = None

class UpdateCard(BaseModel):
    name: Optional[str] = None
    id: Optional[int] = None
    type_attributes: Optional[str] = None
    rarity: Optional[str] = None
    image_url: Optional[str]= None
    play_difficulty: Optional[int] = None
    block_modifier: Optional[int] = None
    block_zone: Optional[str] = None
    description: Optional[list[str]] = None
    symbols: Optional[list[Symbol]] = None
    check: Optional[int] = None
    keyword: Optional[list[str]] = None


class Unicode_Parser():
    def parse_list(self, new_data):
        for number, string in enumerate(new_data):
            unicode = re.search(const.UNICODE_SEARCH, string)
            unicode_swap = None
            print(new_data[number])
            if new_data[number] == "Keywords":
                new_data.pop(number)
            if new_data[number] == "":
                new_data.pop(number)

            if unicode == r"\\u2019":
                unicode_swap = re.sub(unicode, "\'", string)
                append(unicode_swap)         

            if unicode == r"\\u2022":
                unicode_swap = re.sub(unicode, "", string)                
                append(unicode_swap)         

            if unicode == r"\\u201c":
                unicode_swap = re.sub(unicode, "\"", string)
                append(unicode_swap)         
            
            if unicode == r"\\u201d":
                unicode_swap = re.sub(unicode, "\"", string)
                append(unicode_swap)         

            if unicode == r"\\u2022":
                unicode_swap = re.sub(unicode, "", string)
                append(unicode_swap)         
            
            if unicode == True:
                unicode_swap = re.sub(unicode, "", string)
                append(unicode_swap)         
            else:
                print(f"No unicode in string: {string}")    

            print(unicode_swap)
            return unicode_swap
