import os
from pymongo import MongoClient
from pathlib import Path
from dotenv import load_dotenv
from pymongo.collation import Collation


from dotenv import load_dotenv
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME:str = "My Hero API"
    PROJECT_VERSION: str = "1.0.0"

    USER : str = os.getenv("MONGO_USER")
    PASSWORD = os.getenv("MONGO_PWD")
    LOCAL_SERVER : str = "mongodb://localhost:27017"
    LIVE_SERVER = f"mongodb+srv://{USER}:{PASSWORD}@cluster0.itnndfb.mongodb.net/test"
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_REFRESH_SECRET_KEY = os.getenv("JWT_REFRESH_SECRET_KEY")
    JWT_VERFICATION_SECRET = os.getenv("JWT_VERFICATION_SECRET")
    JWT_PASSRESET_SECRET = os.getenv("JWT_PASSRESET_SECRET")
    ALGORITHM = os.getenv("ALGO")
    ACCESS_TOKEN_EXPIRE_MINUTES: int =  60
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  #7 days
    TEST_USER_EMAIL = "test@example.com"

    CLIENT = MongoClient(LIVE_SERVER)
    DB = CLIENT['carddb']
    USER_COLL = DB['user']
    CARD_COLL = DB['card']
    VERIFY_COLL = DB['verification_token']
    PASSRESET_COLL = DB['password_reset_token']

    # - searches for matches that are case sensitive in MongoDB
    SENSITIVE = Collation(
                    locale = "en_US",
                    strength = 3,
                    numericOrdering = True,
                    backwards = False
                )
                
    # - searches for matches that are case insensitive in MongoDB
    INSENSITIVE = Collation(
                    locale = "en_US",
                    strength = 1,
                    numericOrdering = True,
                    backwards = False
                )
    ORIGINS = [
        "http://localhost:3000",
        "https://localhost:3000",
        "http://localhost",
        "http://localhost:8080",
    ]


class GoogleInfo:
    INFO = {
        "email_password": os.getenv("GMPASSWORD"),
        "email_sender": os.getenv("SENDER"),
        "sender_name": os.getenv("SENDER_NAME")
    }

settings = Settings()
ginfo = GoogleInfo()