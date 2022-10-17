from backend.schemas.security_classes import User
from schemas.users import UserCreate
from dependencies.security_funct import get_current_active_user
from fastapi import Depends, Form, APIRouter


router = APIRouter()


# -- All of the different get and post request for authentication --


@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user = user, db = db)
    return user

@router.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username":  username}



@router.get("/me/", response_model = User)
async def read_current_user(current_user: User = Depends(get_current_active_user)):
    return current_user

