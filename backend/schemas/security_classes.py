import os
from pydantic import AnyHttpUrl, BaseModel, BaseSettings
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(BaseModel):
    username: str
    email: str
    hashed_password: str
    is_active: bool
    is_superuser: bool

class UserInDB(User):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class Hasher():
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password):
        return pwd_context.hash(password, secret=settings.JWT_SECRET_KEY)


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY")
    JWT_REFRESH_SECRET_KEY: str = os.getenv("JWT_REFRESH_SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int =  30
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  #7 days
    PROJECT_NAME: str = "My Hero API"

    #Database
    MONGO_CONNECTION_STRING: str = os.getenv("MONGO_CONNECTION_STRING")

    class Config:
        env_file = ".env"

settings = Settings()