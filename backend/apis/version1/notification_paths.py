from db.repository.token import mark_as_verified, is_valid_token, update_token, change_password
from core.config import settings
from fastapi import APIRouter, HTTPException, status


router = APIRouter()


@router.get("/verify")
async def verify(token: str, email: str):
    # Validate the token
    if not is_valid_token(collection = settings.VERIFY_COLL, token = token, email = email):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Token couldn't be found or has already expired.")

    use_token = update_token(email)
    
    if not use_token:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Token has already been used.")

    # Mark the user as verified
    verified = mark_as_verified(email)
    
    if not verified:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Account already verified")
    

    raise HTTPException(status_code=status.HTTP_202_ACCEPTED, detail="Account has been verified")



@router.get('/reset-password')
async def resetPassword(token: str, email: str, password: str):
    # Validate the token
    if not is_valid_token(collection = settings.PASSRESET_COLL, token = token, email = email):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Token couldn't be found or has already expired.")
    
    # Change the 'used' token from False to True
    use_token = update_token(email)
    
    if not use_token:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Token has already been used.")

    # Change the password
    new_password = change_password(email=email, password=password)

    if not new_password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Unable to update password at this time.")

    # Send success status if password has been changed
    raise HTTPException(status_code=status.HTTP_202_ACCEPTED, detail="Password has been reset.")
