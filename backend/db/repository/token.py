from core.config import settings
from datetime import datetime, timedelta

verification_tokens_collection = settings.VERIFY_COLL



def save_verification_token(email: str, token: str):
    # Save the token to the database
    verification_tokens_collection.insert_one(
        {
            "email": email,
            "token": token,
            "expires_at": datetime.utcnow() + timedelta(hours=24),
        }
    )



def is_valid_verification_token(token: str, email: str):
    # Look up the token in the database
    verification_token = verification_tokens_collection.find({"token": token, "email": email}).collation(settings.INSENSITIVE).limit(1)

    # Check if the token has expired
    if verification_token[0] is None:
        return False
    if verification_token[0]["expires_at"] < datetime.utcnow():
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