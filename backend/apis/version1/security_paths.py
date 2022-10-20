from schemas.security_classes import User
from schemas.users import UserCreate
from db.repository.users import get_current_active_user, create_new_user
from fastapi import Depends, Form, APIRouter, HTTPException
from db.session import user_coll


router = APIRouter()


# -- All of the different get and post request for authentication --


@router.post("/", response_model=UserCreate)
async def create_user(user: UserCreate):
    response = await create_new_user(user.dict())
    if response:
        return response
    raise HTTPException(400, "Bad Request")

@router.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username":  username}



@router.get("/me/", response_model = User)
async def read_current_user(current_user: User = Depends(get_current_active_user)):
    return current_user

