from core.config import settings
from fastapi import HTTPException, status, Header
from datetime import datetime, timedelta
from schemas.schema_token import Hasher, ApiToken
from jose import jwt
from pymongo.errors import PyMongoError
from pydantic import parse_obj_as
import json



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

def encode_tokens(raw_key):
    encoded_api_key = jwt.encode({"api_key": raw_key}, key=settings.JWT_API_SECRET, algorithm=settings.ALGORITHM)
    
    return encoded_api_key



async def decode_tokens(data):
    decoded_api_keys = [{**item, "api_key": jwt.decode(token=item["api_key"], key=settings.JWT_API_SECRET, algorithms=settings.ALGORITHM).get('api_key')} for item in data]

    return decoded_api_keys


def save_api_key(username, token, name, hasExpiration, expiration, status):
    exp_date = None
    api_key = encode_tokens(raw_key=token)
    if hasExpiration:
        expiration = datetime.strptime(expiration, '%Y-%m-%dT%H:%M:%S.%fZ') 
        exp_date = expiration

    settings.API_COLL.insert_one({
        "username": username,
        "key_name": name,
        "exp_date": exp_date,
        "api_key": api_key,
        "key_status": status
    })



def is_valid_api_key(api_key: str = Header(...)):
    parsed_key = parse_obj_as(ApiToken, json.loads(api_key))
    print(f"type is: {type(api_key)}, token is: {api_key}\n\n parsed_key is: {type(parsed_key), parsed_key}")

    key_value = parsed_key.api_key
    key_status = parsed_key.key_status
    has_expiration = parsed_key.has_expiration
    exp_date = parsed_key.exp_date

    if key_status == "inactive":
        return False
    if has_expiration and exp_date < datetime.utcnow():
        return False
    
    key = encode_tokens(raw_key=key_value)

    api_key_in_db = settings.API_COLL.find_one({"api_key": key})
    if not api_key_in_db:
        return False
    
    return True



def change_api_key_status(username, key, status):
    try:
        settings.USER_COLL.find_one_and_update(
            filter={"username": username, "api_keys.api_key": key}, 
            update={'$set': {'api_keys.$.key_status': status}}
        )
        settings.API_COLL.find_one_and_update(
            {"api_key": key}, 
            {'$set': {'key_status': status}}
        )

    except PyMongoError as e:
        raise HTTPException(status_code=400, detail=str(e))



def change_api_key_name(username, key, name):
    try:
        settings.USER_COLL.find_one_and_update(
            filter={"username": username, "api_keys.api_key": key}, 
            update={'$set': {'api_keys.$.key_name': name}}
        )
        settings.API_COLL.find_one_and_update(
            {"api_key": key}, 
            {'$set': {'key_name': name}}
        )

    except PyMongoError as e:
        raise HTTPException(status_code=400, detail=str(e))



def add_api_keys(username, api_keys, key_name, has_expiration, expiration, status):
    # - This adds the api keys to the user database
    try:
        exp_date = None
        if has_expiration:
            expiration = datetime.strptime(expiration, '%Y-%m-%dT%H:%M:%S.%fZ') 
            exp_date = expiration

        keys = encode_tokens(raw_key=api_keys)
        settings.USER_COLL.update_one(
                {"username": username},
                {"$push": {"api_keys": {"api_key": keys, "key_name": key_name, "key_status": status, "has_expiration": has_expiration, "exp_date": exp_date}}}, upsert=True
            ).modified_count

        return {"message": "API key added to user's account"}
    except PyMongoError as e:
        raise HTTPException(status_code=400, detail=str(e))




async def delete_api_key(username, api_key):
    # - This deletes the api keys from the user database and api database

    try:

        settings.USER_COLL.update_one(
            {"username": username, "api_keys.api_key": api_key},
            {"$pull": {"api_keys": {"api_key": api_key}}}
        )
        settings.API_COLL.delete_one({"api_key": api_key})
        
        return {"message": "API key removed from user"}
    except PyMongoError as e:
        raise HTTPException(status_code=400, detail=str(e))