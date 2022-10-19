import os
from pymongo import MongoClient
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'

load_dotenv(dotenv_path=env_path)

USER = os.getenv("MONGO_USER")
PASSWORD = os.getenv("MONGO_PWD")
live_uri = f"mongodb+srv://{USER}:{PASSWORD}@cluster0.itnndfb.mongodb.net/test"
local_uri = "mongodb://localhost:27017"

client = MongoClient(local_uri)
db = client['carddb']
user_coll = db['user']
card_coll = db['card']
