from schemas.schema_user import UserCreate, User
from db.repository.users import get_current_active_user, create_new_user
from fastapi import Depends, APIRouter, HTTPException, status
from core.config import settings


router = APIRouter()

# - searches for matches that are case insensitive in MongoDB



@router.post("/", response_model=UserCreate)
async def create_user(user: UserCreate):
    # - Instance of User Collection in DB
    db = settings.USER_COLL

    # - Makes sure the data matches the User model, hashes the password, then returns data 
    new_user = await create_new_user(user.dict())
    
    # - checks if username or password exists already in the database and will throw exceptions if they do.
    if new_user:
        user_match = db.find({'username': new_user['username']}).collation(settings.SENSITIVE)
        email_match = db.find({'email': new_user['email']}).collation(settings.INSENSITIVE)

        user_record = next(user_match, None)
        email_record = next(email_match, None)
                
        if user_record and email_record: 
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Username and email are already in use.")
        
        elif user_record:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Username is linked to an existing account already.")
        
        elif email_record:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email is linked to an existing account already.")

        else:
            db.insert_one(new_user)
            return(user.dict())

    raise HTTPException(400, "Bad Request")



@router.get("/me/", response_model = User)
async def read_current_user(current_user: User = Depends(get_current_active_user)):
    return current_user

