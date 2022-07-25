from datetime import timedelta
from dependencies.security_classes import Token, User
from dependencies.security_consts import ACCESS_TOKEN_EXPIRE_MINUTES
from dependencies.security_funct import authenticate_user, create_access_token, fake_users_db, get_current_active_user
from fastapi import Depends, HTTPException, Form, APIRouter, status
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()


# -- All of the different get and post request for authentication --

@router.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username":  username}



@router.get("/me/", response_model = User)
async def read_current_user(current_user: User = Depends(get_current_active_user)):
    return current_user

