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



def is_valid_verification_token(email: str, token: str):
    # Look up the token in the database
    verification_token = verification_tokens_collection.find_one(
        {"email": email, "token": token}
    )

    # Check if the token has expired
    if verification_token is None:
        return False
    if verification_token["expires_at"] < datetime.utcnow():
        return False

    return True



def mark_as_verified(email: str):
    # Connect to the database
    users_collection = settings.USER_COLL

    # Find the user with the matching email
    user = users_collection.find_one({"email": email})

    # If the user exists, update their verification status
    if user:
        user["is_verified"] = True
        users_collection.save(user)