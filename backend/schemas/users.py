from beanie import PydanticObjectId
from pydantic import BaseModel, EmailStr, Field
from bson.objectid import ObjectId
import pydantic

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class ShowUser(BaseModel):
    username: str
    email: EmailStr
    is_active: bool

    class Config():
        orm_mode = True
