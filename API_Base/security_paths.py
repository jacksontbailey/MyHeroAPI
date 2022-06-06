from api_base.security_classes import User, UserInDB
from api_base.security_funct import fake_hash_password, fake_users_db, get_current_active_user
from fastapi import Depends, HTTPException, Form, APIRouter
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter()


# -- All of the different get and post request for authentication --

@router.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username":  username}

@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    
    if not user_dict:
        raise HTTPException(status_code = 400, detail = "Username doesn't exist", headers="Username doesn't exist")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)

    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code = 400, detail = "Incorrect username or password", headers="Incorrect username or password")
    
    return {"access_token": user.username, "token_type": "bearer"}



@router.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

