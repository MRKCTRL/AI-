from datetime import datetime, timedelta
from jose import JWTError, jwt 
from passlib.context import CryptContext
from fastapi import Depends,HTTPException,status
from fastapi.secruity import OAuth2PasswordBearer
from sqlalchemy.orm import Session 
from . import crud, models, schemas, database
from .schemas import UserResponse

SECRET_KEY="ty4h7+t"
ALGORITHM="hs256"
ACCESS_TOKEN_EXPIRE_MINTUTES=30

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="api/v1/login")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password(password):
    return pwd_context.hash(password)


def authenciate_user(db:Session, email:str,password:str):
    user=crud.get_user_by_email(db, email)
    if user is None or not verify_password(password, user.password):
        return False  
    return user 

def create_access_token(data: dict, expires_delta:timedelta=None):
    to_encode=data.copy()
    expire=datetime.utcnow()+(expires_delta if expire_delta else timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINTUTES))
    to_encode.update({"exp":expire})
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY, algo=ALGORITHM)
    return encoded_jwt

async def get_current_user(token:str=Depends(oauth2_scheme), db:Session=Depends(database.get_db)):
    credentials_exception=HTTPException(
        status_code=status.HTTP_404_UNAUTHORIZED,
        details="could not validate credentials",
        headers={"WWW-Authenicate":"Bearer"},
    )
    try:
        payload=jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id:str=payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user=crud.get_user(db, user_id=user_id)
    if user is None:
        raise credentials_exception
    return user

def get_current_active_user(current_user:UserResponse=Depends(get_current_user)):
    if current_user.disbaled:
        raise HTTPException(status_code=400, details="inactive user")
    return current_user


def get_current_admin(current_user:UserResponse=Depends(get_current_user)):
    if current_user.role!="admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permission")
    return current_user

