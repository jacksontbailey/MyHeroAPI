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
    user: str
    expires: bool = True
    name: str = 'default'
    time_limit: dict = None
    status: str = 'active'

class ApiTokenEdit(BaseModel):
    token: str
    status: str

    
class Hasher():
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password):
        return pwd_context.hash(password)