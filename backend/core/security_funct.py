import os
from datetime import datetime, timedelta
from core.config import settings
from jose import jwt, JWTError


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.ALGORITHM)
    
    return encoded_jwt


def create_refresh_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta is not None:
        expires = datetime.utcnow() + expires_delta
    else:
        expires = datetime.utcnow() + timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expires})
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt




def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=settings.ALGORITHM)
        return payload
    except JWTError as e:
        raise e


def verify_refresh_token(token: str):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=settings.ALGORITHM)
        return payload
    except JWTError as e:
        raise e



def generate_token(email: str, secret: str):
    token = jwt.encode(
        {
            "sub": email,
            "exp": datetime.utcnow() + timedelta(hours=24),
        },
        key=secret,
        algorithm=settings.ALGORITHM,
    )
    return token



def generate_random_token():
    random_string = os.urandom(24).hex()
    return random_string
