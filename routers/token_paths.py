from datetime import timedelta
from dependencies.security_classes import Token
from dependencies.security_consts import ACCESS_TOKEN_EXPIRE_MINUTES
from dependencies.security_funct import authenticate_user, create_access_token, fake_users_db
from fastapi import Depends, HTTPException, APIRouter, status
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post("", response_model = Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)

    if not user:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail= "Incorrect username or password",
            headers= {"WWW-Authenticate": "Bearer"}
        )
    access_token_expires = timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data = {"sub": user.username}, expires_delta = access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}