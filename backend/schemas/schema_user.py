from pydantic import BaseModel, EmailStr


class User(BaseModel):
    username: str
    email: str
    hashed_password: str
    is_active: bool
    is_superuser: bool
    is_verified: bool

class UserWithKeys(User):
    api_keys: list | None = []

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserPassChange(BaseModel):
    email: str

class UserPassReset(BaseModel):
    token: str
    email: EmailStr
    password: str

class ShowUser(BaseModel):
    username: str
    email: EmailStr
    is_active: bool

    class Config():
        orm_mode = True


class UserInDB(User):
    hashed_password: str