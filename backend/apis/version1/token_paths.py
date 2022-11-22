from datetime import timedelta
from schemas.schema_token import Token
from schemas.schema_user import User
from core.security_funct import create_access_token
from core.config import settings
from db.repository.users import authenticate_user, get_current_active_user
from fastapi import Depends, HTTPException, APIRouter, status
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post("", response_model = Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)

    if not user:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail= "Incorrect username or password",
            headers= {"WWW-Authenticate": "Bearer"}
        )
    access_token_expires = timedelta(minutes = settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    refresh_token_expires = timedelta(minutes = settings.REFRESH_TOKEN_EXPIRE_MINUTES)

    access_token = create_access_token(
        data = {"sub": user.username}, expires_delta = access_token_expires
    )
    refresh_token = create_access_token(
        data = {"sub": user.username}, expires_delta = refresh_token_expires
    )

    print({"access_token": access_token, "token_type": "bearer"})
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}

@router.get("/me", response_model = User)
async def read_current_user(current_user: User = Depends(get_current_active_user)):
    return current_user