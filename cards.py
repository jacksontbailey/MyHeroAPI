import re
import unicodedata

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
    def __init__(self) -> None:
        pass

    def ascii_code(self, item):
        print(f"{item}: {type(item)}")

        initial_match = re.search(const.UNICODE_SEARCH, item)
        if initial_match != None:
            matches = re.findall(const.UNICODE_SEARCH, item)

            # -- If any ASCII (unicode) is spotted, this will replace it.
            for match in matches:
                    
                if unicodedata.name(match) == "BULLET":
                    c = re.sub(match, "", item)
                    return(c)
                else:
                    print("returned regular item")
                    return(item)
        else:
            print(f"Item didn't have ascii code match: {item}")
            return(item)
    
    def space_matcher(self, item, previous_item):
        space_match = re.search(const.SPACE_DIGIT, item)
        # -- Checks to see if the item in the list starts out with a space & number. If it does, then it 
        # -- takes that number and puts it on the previous item in the list and updates the current list.
        # -- I'm doing this because some of the data from TCG player doesn't properly sort the keywords and seperates the items incorrectly.
        if space_match != None:
            start = space_match.start()
            end = space_match.end()
            save_array_item = item[start:end]
            new_save= str(save_array_item).replace(" ", "")
            
            delete_item_from_current_array = re.sub(r"(^ \d )", "", item)
            updated_previous_item = f"{previous_item}: {new_save}"

            previous_item = updated_previous_item
            item = delete_item_from_current_array
            print(f"{item}: is item. {previous_item}: is previous item")
            return(item, previous_item)
        else:
            print(f"No match, but {item}: is item. {previous_item}: is previous item")
            return(item, previous_item)
    
    def unwanted_match(self, item):
        
        item = re.sub(const.SPACE_START, "", item)
        
        # -- Gets rid of list items that just say "Keywords"    
        if item == "Keywords":
            return(None)
        
        # -- Gets rid of empty list items
        if item == "" or item == '':
            return(None)


        return item

    def delete_none(self, data):
        for num, item in enumerate(data):
            if item == None:
                print(f"Popping item ({item}) from list")
                data.pop(num)
            
        return(data)


    
    def parse_list(self, new_data):
        print(new_data)

        for number, string in enumerate(new_data):
            previous_array_item = new_data[number-1]

            print(f"Here is the string: {string}")
            ascii_code_checker = self.ascii_code(string)
            print(f"parse_list: finished ascii_code_checker. Var is: {ascii_code_checker}")
            space_code_checker = self.space_matcher(ascii_code_checker, previous_array_item)
            new_data[number-1]=space_code_checker[1]
            unwanted_code_checker = self.unwanted_match(space_code_checker[0])

            new_data[number] = unwanted_code_checker
            print(f"Unicode Swap 2: {unwanted_code_checker}")
            
            print(f"New data: {new_data}")
        new_data = self.delete_none(new_data)
        print(new_data)