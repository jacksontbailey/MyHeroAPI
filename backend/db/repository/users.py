import json

from schemas.security_classes import *
from schemas.users import UserCreate
from db.session import user_coll
from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/token"
    )


def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    
    if not Hasher.verify_password(user.hashed_password, Hasher.get_password_hash(password)):
        return False
    
    return user



def get_user(username: str, db = user_coll):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)



async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[status.ALGORITHM])
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



async def create_new_user(user, db = user_coll):

    print(f"user is {type(user), user}\n username data is: {type(user['username']), user['username']}\n Password is: {type(user['password']), user['password']} \n Email is {type(user['email']), user['email']}")
    new_user = User(
        username = user['username'],
        email = user['email'],
        hashed_password = Hasher.get_password_hash(user['password']),
        is_active = True,
        is_superuser = False,
        ).dict()
    print(type(new_user), new_user)

    db.insert_one(new_user)
    return(user)