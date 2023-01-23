from core.config import settings
from fastapi import HTTPException
from datetime import datetime, timedelta
from schemas.schema_token import Hasher
from jose import jwt
from pymongo.errors import PyMongoError



def save_verification_token(collection, email: str, token: str):
    # Save the token to the database
    collection.insert_one(
        {
            "email": email,
            "expires_at": datetime.utcnow() + timedelta(hours=24),
            "token": token,
            "used": False
        }
    )


def is_valid_token(collection, token: str, email: str):
    # Look up the token in the database
    token_array = collection.find({"token": token, "email": email}).collation(settings.INSENSITIVE).limit(1)
    verification_token = token_array[0]
    # Check if the token exists, has expired, or already been used
    if verification_token is None:
        return False
    if verification_token["expires_at"] < datetime.utcnow():
        return False
    if verification_token["used"] is True:
        return False

    return True
    


def mark_as_verified(email: str):
    # Connect to the database
    users_collection = settings.USER_COLL

    # Find the user with the matching email. If the user exists, update their verification status
    verified_user = users_collection.find_one_and_update(
        filter = {"email" : email, 'is_verified': False},
        update = {"$set": {'is_verified': True}},
        return_document=True
    )

    return verified_user


def update_token(collection, email: str):
    # Connect to the database
    token_collection = collection
    
    # Find the token with the matching email and update it's used status"
    updated_token = token_collection.find_one_and_update(
        filter = {"email" : email, 'used': False},
        update = {"$set": {'used': True}}
    )

    return updated_token



def change_password(email: str, password: str):
    # Encrypt the password
    hashed_password = Hasher.get_password_hash(password=password)

    # Connect to the database
    users_collection = settings.USER_COLL

    # Find the user with the matching email. If the user exists, update their verification status
    password_change = users_collection.find_one_and_update(
        filter = {"email" : email},
        update = {"$set": {'hashed_password': hashed_password}},
        return_document=True
    )

    return password_change


# - For API Tokens JWT_API_SECRET

async def save_api_key(username, token, name, hasExpiration, expiration, status):
    exp_date = None
    print(f"user = {username}, token = {token}, name = {name}, hasExpiration = {hasExpiration}, expiration = {expiration}, status = {status}")
    if hasExpiration:
        expiration = datetime.strptime(expiration, '%Y-%m-%dT%H:%M:%S.%fZ') 
        exp_date = expiration

    settings.API_COLL.insert_one({
        "user": username,
        "name": name,
        "exp_date": exp_date,
        "token": jwt.encode({'token': token}, settings.JWT_API_SECRET, algorithm=settings.ALGORITHM),
        "status": status
    })



def is_valid_api_key(token):
    api_key = settings.API_COLL.find_one({"token": token})
    if not api_key:
        return False
    decoded_token = jwt.decode(api_key["token"], settings.JWT_API_SECRET, algorithms=settings.ALGORITHM)
    token = decoded_token["token"]
    if api_key["status"] == "deactivated":
        return False
    if api_key["exp_date"] and api_key["exp_date"] < datetime.utcnow():
        return False
    return True


def change_api_key_status(token, status):
    api_key = settings.API_COLL.find_one({"token": token})
    decoded_token = jwt.decode(api_key["token"], settings.JWT_API_SECRET, algorithms=settings.ALGORITHM)
    token = decoded_token["token"]
    settings.API_COLL.update_one({"token": token}, {"$set": {"status": status}})



async def add_api_keys(username, api_keys):
    # - This adds the api keys to the user database
    try:
        keys = jwt.encode({'token': api_keys}, settings.JWT_API_SECRET, algorithm=settings.ALGORITHM)
        settings.USER_COLL.update_one(
            {"username": username},
            {"$push": {"api_keys": {"$each": [keys]}}}
        )
        return {"message": "API keys added to user"}
    except PyMongoError as e:
        raise HTTPException(status_code=400, detail=str(e))




async def delete_api_key(username, api_key):
    # - This deletes the api keys from the user database and api database

    try:
        settings.USER_COLL.update_one(
            {"username": username},
            {"$pull": {"api_keys": api_key}}
        )
        settings.API_COLL.delete_one({"token": api_key})
        return {"message": "API key removed from user"}
    except PyMongoError as e:
        raise HTTPException(status_code=400, detail=str(e))