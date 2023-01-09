from core.config import settings
from datetime import datetime, timedelta
from schemas.schema_token import Hasher


def save_token(collection, email: str, token: str):
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
