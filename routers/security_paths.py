from datetime import timedelta
from dependencies.security_classes import Token, User
from dependencies.security_consts import ACCESS_TOKEN_EXPIRE_MINUTES
from dependencies.security_funct import authenticate_user, create_access_token, fake_users_db, get_current_active_user
from fastapi import Depends, HTTPException, Form, APIRouter, status
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/users",
    tags=["security"]
)


# -- All of the different get and post request for authentication --

@router.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username":  username}

@router.post("/token", response_model = Token)
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
        data = {"sub": user.username, "scopes": form_data.scopes},
        expires_delta = access_token_expires,
    )
    
    return {"access_token": access_token, "token_type": "bearer"}



@router.get("/me", response_model = User)
async def read_current_user(current_user: User = Depends(get_current_active_user)):
    return current_user

