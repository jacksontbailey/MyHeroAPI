from datetime import datetime, timedelta
from dependencies.constants import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, JWT_REFRESH_SECRET_KEY, JWT_SECRET_KEY, REFRESH_TOKEN_EXPIRE_MINUTES
from jose import jwt



# -- Token Authentication Functions
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    print(f"Algorithm: {ALGORITHM}")
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt


def create_refresh_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta is not None:
        expires = datetime.utcnow() + expires_delta
    else:
        expires = datetime.utcnow() + timedelta(minutes= REFRESH_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expires})
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, algorithm = ALGORITHM)
    
    return encoded_jwt