from db.repository.token import mark_as_verified, is_valid_verification_token
from fastapi import APIRouter, HTTPException, status


router = APIRouter()


@router.get("/verify")
async def verify(token: str, email: str):
    # Validate the token
    if not is_valid_verification_token(token, email):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Token couldn't be found or has already expired.")


    # Mark the user as verified
    verified = mark_as_verified(email)
    print(f'verified route is {verified}')
    
    if not verified:
        print("returning error")
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Account already verified")
    print("returning success")    
    
    raise HTTPException(status_code=status.HTTP_202_ACCEPTED, detail="Account has been verified")
    