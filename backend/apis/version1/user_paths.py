from schemas.schema_user import UserCreate, UserPassChange
from db.repository.users import create_new_user
from fastapi import APIRouter, HTTPException, status, BackgroundTasks
from core.config import settings
from core.background import send_verification_email


router = APIRouter()

# - searches for matches that are case insensitive in MongoDB

@router.post("", response_model=UserCreate)
async def create_user(user: UserCreate, background_tasks: BackgroundTasks):
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
            # Insert new user into database
            db.insert_one(new_user)

            # Send verification email to new user to activate account
            background_tasks.add_task(send_verification_email, email = new_user['email'], host = settings.ORIGINS[0])
            
            return(user.dict())

    raise HTTPException(400, "Bad Request")


@router.post("/password", response_model=UserPassChange)
async def forgotPassword(email: UserPassChange, background_tasks: BackgroundTasks):
    # - Instance of User Collection in DB
    db = settings.USER_COLL
    
    email_match = db.find({'email': email['email']}).collation(settings.INSENSITIVE)

    if not email_match:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Email not found.")
    else:
        background_tasks.add_task(send_verification_email, email = email['email'], host = settings.ORIGINS[0])


