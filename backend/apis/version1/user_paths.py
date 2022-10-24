from schemas.schema_user import UserCreate, User
from db.repository.users import get_current_active_user, create_new_user
from fastapi import Depends, APIRouter, HTTPException, status
from pymongo.collation import Collation
from core.config import settings


router = APIRouter()

i_case = Collation(
                    locale = "en_US",
                    strength = 1,
                    numericOrdering = True,
                    backwards = False
                )

s_case = Collation(
                    locale = "en_US",
                    strength = 3,
                    numericOrdering = True,
                    backwards = False
                )


# -- All of the different get and post request for authentication --


@router.post("/", response_model=UserCreate)
async def create_user(user: UserCreate):
    user_exists = False
    db = settings.USER_COLL

    new_user = await create_new_user(user.dict())
    
    if new_user:
        user_match = db.find({'username': new_user['username']}).collation(i_case)
        email_match = db.find({'email': new_user['email']}).collation(i_case)

        user_record = next(user_match, None)
        email_record = next(email_match, None)
                
        if user_record and email_record: 
            user_exists = True
            print(user_match)
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Username and email are already in use.")
        
        elif user_record:
            user_exists = True
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Username is linked to an existing account already.")
        
        elif email_record:
            user_exists = True
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email is linked to an existing account already.")

        elif user_exists == False:
            db.insert_one(new_user)
            return(user.dict())

    raise HTTPException(400, "Bad Request")


@router.get("/me/", response_model = User)
async def read_current_user(current_user: User = Depends(get_current_active_user)):
    return current_user

