import os
from pymongo import MongoClient
from pathlib import Path
from dotenv import load_dotenv
from schemas.security_classes import *

env_path = Path('.') / '.env'

load_dotenv(dotenv_path=env_path)

USER = os.getenv("MONGO_USER")
PASSWORD = os.getenv("MONGO_PWD")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_REFRESH_SECRET_KEY = os.getenv("JWT_REFRESH_SECRET_KEY")
ALGORITHM = os.getenv("ALGO")
ACCESS_TOKEN_EXPIRE_MINUTES: int =  30
REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  #7 days


LIVE_SERVER = f"mongodb+srv://{USER}:{PASSWORD}@cluster0.itnndfb.mongodb.net/test"
LOCAL_SERVER = "mongodb://localhost:27017"

CLIENT = MongoClient(LOCAL_SERVER)
DB = CLIENT['carddb']
USER_COLL = DB['user']
CARD_COLL = DB['card']