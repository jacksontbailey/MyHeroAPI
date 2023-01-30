from pydantic import BaseModel
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class AccessTokenRefreshed(BaseModel):
    access_token: str
    token_type: str | None = None


class ApiTokenCreate(BaseModel):
    name: str | None = 'default'
    hasExpiration: bool | None = False
    expiration: str | None = None
    username: str
    status: str | None = 'active'

class ApiTokenEdit(BaseModel):
    api_key: str
    key_name: str
    key_status: str
    has_expiration: bool
    exp_date: str | None = None

    
class Hasher():
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password):
        return pwd_context.hash(password)