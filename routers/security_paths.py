from dependencies.security_classes import User
from dependencies.security_funct import get_current_active_user
from fastapi import Depends, Form, APIRouter 

router = APIRouter()


# -- All of the different get and post request for authentication --

@router.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username":  username}



@router.get("/me/", response_model = User)
async def read_current_user(current_user: User = Depends(get_current_active_user)):
    return current_user

