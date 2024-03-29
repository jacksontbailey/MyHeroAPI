from schemas.schema_token import Hasher, TokenData
from core.config import settings
from schemas.schema_user import User, UserInDB, UserWithKeys
from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/login"
    )



def authenticate_user(username: str, password: str):
    user = get_user(username)

    if not user:
        return False
    
    if not Hasher.verify_password(password, user.hashed_password):
        return False
    
    return user



def check_verification_status(username: str):
    user=get_user(username)

    if not user.is_verified:
        return False
    
    return True



def get_user(username: str | None = None, email: str | None = None, db = settings.USER_COLL):
    # Create the query dictionary
    query = {}
    if username:
        query["username"] = username
    if email:
        query["email"] = email

    # Find the user
    document = db.find_one(query)

    # Return the user as a UserInDB object if it exists
    if document:
        return UserInDB(**document)



async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(username = token_data.username)
    if user is None:
        raise credentials_exception
    return user



async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code = 400, detail = "Inactive user")
    return current_user



async def check_if_user_is_admin(current_user: User = Depends(get_current_active_user)) -> User:
    if not current_user.is_superuser:
        raise HTTPException(status_code=401, detail="You have not enough privileges")
    return current_user



async def create_new_user(user):
    new_user = UserWithKeys(
        username = user['username'],
        email = user['email'],
        hashed_password = Hasher.get_password_hash(user['password']),
        is_active = True,
        is_superuser = False,
        is_verified = False,
        api_keys = []
        ).dict()
    
    return(new_user)


async def remove_user(id):
    await settings.USER_COLL.delete_one({"_id": f"ObjectId('{id}')"})
    return True