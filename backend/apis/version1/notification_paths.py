from db.repository.token import mark_as_verified, is_valid_verification_token
from fastapi import APIRouter


router = APIRouter()


@router.get("/verify")
def verify(email: str, token: str):
    # Validate the token
    if not is_valid_verification_token(email, token):
        return {"error": "Invalid token"}

    # Mark the user as verified
    mark_as_verified(email)
    return {"message": "Successfully verified"}