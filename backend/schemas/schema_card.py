import re, unicodedata

from pyparsing import Opt

import web_scraper.constants as const
from enum import Enum
from typing import Annotated, Optional, Literal, Union
from pydantic import BaseModel, Field, HttpUrl, Json, ValidationError, validator
from starlette.requests import Request

class LowerCaseMiddleware:
    def __init__(self) -> None:
        self.DECODE_FORMAT = "latin-1"

    async def __call__(self, request: Request, call_next):
        raw = request.scope["query_string"].decode(self.DECODE_FORMAT).lower()
        request.scope["query_string"] = raw.encode(self.DECODE_FORMAT)

        path = request.scope["path"].lower()
        request.scope["path"] = path

        response = await call_next(request)
        return response

class Zone(str, Enum):
    high = "High"
    low = "Low"
    mid = "Mid"

class Symbol(str, Enum):
    air = "Air"
    all = "All"
    chaos = "Chaos"
    death = "Death"
    earth = "Earth"
    evil = "Evil"
    fire = "Fire"
    good = "Good"
    infinity = "Infinity"
    life = "Life"
    order = "Order"
    void = "Void"
    water = "Water"


class Set(str, Enum):
    s1 = "My Hero Academia"
    s2 = "Crimson Rampage"
    special = "Provisional Showdown"

class CharacterCard(BaseModel):
    max_health: int
    starting_hand_size: int
    type: Literal['Character']


class AttackCard(BaseModel):
    ability: str | None
    attack_keywords: list[str] | None
    attack_zone: Zone
    damage: int
    speed: int
    type: Literal['Attack']

class FoundationCard(BaseModel):
    type: Literal['Foundation']

class ActionCard(BaseModel):
    type: Literal['Action']

class AssetCard(BaseModel):
    type: Literal['Asset']


class AllCards(BaseModel):

    id: int
    name: str
    url: str

class Card(BaseModel):
    block_modifier: int
    block_zone: str
    check: int
    description: list[str | list[str]] | None = None
    id: int
    image_url: HttpUrl | None = None
    keyword: list[str] | None = None
    name: str
    play_difficulty: int
    rarity: str
    set: Set
    symbols: list[Symbol]
    type_attributes: Annotated[Union[CharacterCard, AttackCard, AssetCard, ActionCard, FoundationCard], Field(discriminator='type')] | None = None

    class Config:
        case_sensitive = False
        orm_mode = True


class UpdateCard(BaseModel):
    block_modifier: Optional[int] = None
    block_zone: Optional[str] = None
    check: Optional[int] = None
    description: Optional[list[str]] = None
    id: Optional[int] = None
    image_url: Optional[HttpUrl]= None
    keyword: Optional[list[str]] = None
    name: Optional[str] = None
    play_difficulty: Optional[int] = None
    rarity: Optional[str] = None
    set: Optional[Set] = None
    symbols: Optional[list[Symbol]] = None
    type_attributes: Optional[Annotated[Union[CharacterCard, AttackCard, AssetCard, ActionCard, FoundationCard], Field(discriminator='type')]] = None

    class Config:
        orm_mode = True

class Unicode_Parser():
    def __init__(self) -> None:
        pass


    def ascii_code(self, item):
        initial_match = re.search(const.UNICODE_SEARCH, item)
        
        if initial_match != None:
            matches = re.findall(const.UNICODE_SEARCH, item)

            # -- If any ASCII (unicode) is spotted, this will replace it.
            for match in matches:
                    
                if unicodedata.name(match) == "BULLET":
                    c = item.split(match, -1)
                    return(c, True)
                elif unicodedata.name(match) == "MIDDLE DOT":
                    c = item.split(match, -1)
                    return(c, True)
                elif unicodedata.name(match) == "RIGHT SINGLE QUOTATION MARK":
                    c = item.replace(match, r"\'")
                    return(item, True)
                elif unicodedata.name(match) == ("RIGHT DOUBLE QUOTATION MARK" | "LEFT DOUBLE QUOTATION MARK"):
                    c = item.replace(match, r"\"")
                    return(item, True)
                else:
                    print(f"There was a unicode match not listed: {unicodedata.name(match)}")
                    return(item, False)
        else:
            return(item, False)
    

    def space_matcher(self, item, previous_item):
        # -- Checks to see if the item in the list starts out with a space & number. If it does, then it 
        # -- takes that number and puts it on the previous item in the list and updates the current list.
        # -- I'm doing this because some of the data from TCG player doesn't properly sort the keywords and seperates the items incorrectly.
        number_space_match = re.search(const.SPACE_DIGIT, item)
        if number_space_match != None:
            start = number_space_match.start()
            end = number_space_match.end()
            save_array_item = item[start:end]
            new_save= str(save_array_item).replace(" ", "")
            
            delete_item_from_current_array = re.sub(const.SPACE_DIGIT, "", item)
            updated_previous_item = f"{previous_item}: {new_save}"

            previous_item = updated_previous_item
            item = delete_item_from_current_array

        
        regular_space_match = re.search(const.SPACE_START_END, item)
        if regular_space_match != None:
            item = re.sub(const.SPACE_START_END, "", item)
        return(item, previous_item)
    

    def unwanted_match(self, item):
                
        # -- Gets rid of list items that just say "Keywords"    
        if item == "Keywords":
            return(None)
        
        # -- Gets rid of empty list items
        if item == "" or item == '':
            return(None)


        return item


    def delete_none(self, data):
        for num, item in reversed(list(enumerate(data))):
            if item == None:
                data.pop(num)
        return(data)


    def parse_string(self, new_string):
        parse_new_string = new_string
        string_boolean_checker = True

        while string_boolean_checker == True:
            parse_new_string = self.ascii_code(parse_new_string[0])
            string_boolean_checker = parse_new_string[1]

        return parse_new_string
    

    def parse_list(self, new_data):
        parse_new_data = new_data
        print(f"Old data: {parse_new_data}")
        for number, string in enumerate(parse_new_data):

            ascii_code_checker = self.ascii_code(string)
            
            if ascii_code_checker[1] == True:
                parse_new_data[number+1:number+1]= ascii_code_checker[0]
                parse_new_data.pop(number)

            previous_array_item = parse_new_data[number-1]

            space_code_checker = self.space_matcher(parse_new_data[number], previous_array_item)
            parse_new_data[number-1]=space_code_checker[1]

            unwanted_code_checker = self.unwanted_match(space_code_checker[0])

            parse_new_data[number] = unwanted_code_checker
            
        parse_new_data = self.delete_none(parse_new_data)
        print(f"New data: {parse_new_data}")
        return parse_new_data