from schemas.security_classes import User
from schemas.users import UserCreate
from db.repository.users import get_current_active_user, create_new_user
from fastapi import Depends, Form, APIRouter
from db.session import client


router = APIRouter()


# -- All of the different get and post request for authentication --


@router.post("/")
def create_user(user: UserCreate, db: client):
    user = create_new_user(user = user, db = db)
    return user

@router.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username":  username}



@router.get("/me/", response_model = User)
async def read_current_user(current_user: User = Depends(get_current_active_user)):
    return current_user

