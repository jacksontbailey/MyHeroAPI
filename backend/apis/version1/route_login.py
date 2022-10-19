from datetime import datetime, timedelta

from schemas.security_classes import *
from fastapi import HTTPException, Depends, status, APIRouter
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/token"
    )
router = APIRouter()


def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    
    if not Hasher.verify_password(user.hashed_password, Hasher.get_password_hash(password)):
        return False
    
    return user



def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)



async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms = [status.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user(username = username, db = db)
    if user is None:
        raise credentials_exception
    return user



async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code = 400, detail = "Inactive user")
    return current_user