import json
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

def test_create_user(client):
    data = {"username":"testuser", "full_name":"Test User", "email":"testuser@nofoobar.com","password":"testing", "disabled": False}
    response = client.insert_one(data).inserted_id
    assert response.json()["email"] == "testuser@nofoobar.com"
    assert response.json()["is_active"] == True


test_create_user(client=user_coll)

client.close()