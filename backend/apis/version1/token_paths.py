from datetime import timedelta
from schemas.schema_token import Token, AccessTokenRefreshed
from schemas.schema_user import User
from core.security_funct import create_access_token, verify_refresh_token, create_refresh_token
from core.config import settings
from db.repository.users import authenticate_user, get_current_active_user, check_verification_status, get_user
from fastapi import Depends, HTTPException, APIRouter, status
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post("", response_model = Token, include_in_schema=False)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)

    if not user:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail= "Incorrect username or password",
            headers= {"WWW-Authenticate": "Bearer"}
        )
    
    verified = check_verification_status(form_data.username)

    if not verified:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail= "Account hasn't been verified. Please click the link in your email to verify your account.",
            headers={"WWW-Authenticate": "Bearer"}
        )

    access_token_expires = timedelta(minutes = settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    refresh_token_expires = timedelta(minutes = settings.REFRESH_TOKEN_EXPIRE_MINUTES)

    access_token = create_access_token(
        data = {"sub": user.username}, expires_delta = access_token_expires
    )
    refresh_token = create_refresh_token(
        data = {"sub": user.username}, expires_delta = refresh_token_expires
    )

    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}



@router.post("/refresh", response_model=AccessTokenRefreshed, include_in_schema = False)
async def refresh_access_token(refresh_token: str):
    try:
        payload = verify_refresh_token(refresh_token)
    except Exception as error:
        return error

    username = payload.get("sub")
    
    if not username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    user = get_user(username=username)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes = settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
            data={"sub": user.username}, expires_delta=access_token_expires
        )
    
    return {"access_token": access_token, "token_type": "bearer"}



@router.get("/me", response_model = User)
async def read_current_user(current_user: User = Depends(get_current_active_user)):
    return current_user