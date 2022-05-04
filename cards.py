import re
import card_page.constants as const
from enum import Enum
from typing import Optional
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
    type = "Character"
    starting_hand_size: int
    max_health: int

class AttackCard(str, Enum):
    type = "Attack"
    zone = "High" or "Mid" or "Low"
    speed: int
    damage: int
    keyword: list[AttackKeyword]
    ability: Optional[str]

class CardType(str, Enum):
    character = list[CharacterCard]
    attack = list[AttackCard]
    foundation = "Foundation"
    action = "Action"
    assets = "Asset"

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
    keyword: Optional[list] | None = None

class UpdateCard(BaseModel):
    id: Optional[int] = None
    image_url: Optional[str]= None
    name: Optional[str] = None
    type: Optional[CardType] = None
    rarity: Optional[str] = None
    play_difficulty: Optional[int] = None
    block_modifier: Optional[int] = None
    block_zone: Optional[str] = None
    text_box: Optional[list[str]] = None
    symbols: Optional[list[Symbol]] = None
    check: Optional[int] = None
    keyword: Optional[list[str]] = None



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

                



