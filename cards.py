import re
import card_page.constants as const
from enum import Enum
from typing import Optional, Literal, Union
from pydantic import BaseModel, ValidationError, validator

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

class Card(BaseModel):
    name: str
    id: int
    rarity: str
    image_url: str | None = None
    play_difficulty: int
    block_modifier: int
    block_zone: str
    text_box: list[str]
    symbols: list[Symbol]
    check: int
    keyword: Optional[list] | None = None

class UpdateCard(BaseModel):
    id: Optional[int] = None
    image_url: Optional[str]= None
    name: Optional[str] = None
    rarity: Optional[str] = None
    play_difficulty: Optional[int] = None
    block_modifier: Optional[int] = None
    block_zone: Optional[str] = None
    text_box: Optional[list[str]] = None
    symbols: Optional[list[Symbol]] = None
    check: Optional[int] = None
    keyword: Optional[list[str]] = None

class CharacterCard(Card):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()

    type = "Character"
    starting_hand_size: int
    max_health: int

class AttackCard(Card):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()

    type = "Attack"
    zone = "High" or "Mid" or "Low"
    speed: int
    damage: int
    keyword: list[AttackKeyword]
    ability: Optional[str]

class FoundationCard(Card):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()
    
    type = "Foundation"
class ActionCard(Card):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()
    
    type = "Action"
class AssetCard(Card):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()
    
    type = "Asset"

class Unicode_Parser():

    def parse_list(self, new_data):
        for number, string in enumerate(new_data):
#            if (new_data[number] == "Keywords") | (new_data[number] == ""):
#                print(f"{string} is a keyword")

            unicode = re.search(const.UNICODE_SEARCH, string)

            if unicode == r"\u2019":
                unicode_swap = re.sub(unicode, "\'", string)
                return(unicode_swap)

            elif unicode == r"\u2022":
                unicode_swap = re.sub(unicode, "", string)                
                return(unicode_swap)

            elif unicode == r"\u201c":
                unicode_swap = re.sub(unicode, "\"", string)
                return(unicode_swap)
            
            elif unicode == r"\u201d":
                unicode_swap = re.sub(unicode, "\"", string)
                return(unicode_swap)

            elif unicode == r"\u2022":
                unicode_swap = re.sub(unicode, "", string)
                return(unicode_swap)
            else:
                print(f"No unicode in string: {string}")    

                
    
class Height(str, Enum):
    tall = "tall"
    medium = "medium"
    short = "short"
class Parent_Class(BaseModel):
    eyes: str
    height: Height
    weight: int

class Child_Class(Parent_Class):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()
    name: str = "Peter"
    
