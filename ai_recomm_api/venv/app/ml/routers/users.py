from fastapi import APIRouter, Depends, HttpException,status
from sqlalchemy.orm import Session 
from .. import schemas, crud, database
from fastapi.secruity  import OAuth2PasswordRequest
from .. import schemas,crud,database,auth


router=APIRouter()

@router.post("/users/", response_model=schemas.UserResponse)
def create_user(user:schemas.UserCreate, db:Session=Depends(database.get_db)):
    return crud.create_user(db=db,user=user)

@router.get("/users/{user_id}", response_model=schemas.UserResponse)
def get_user(user_id:int, db:Session=Depends(database.get_db)):
    db_user=crud.get_user(db,user_id=user_id)
    if db_user is None:
        raise HttpException(status_code=404, detail="user not found")
    return db_user
        

@router.post("/register/", response_model=schemas.UserResponse)
def register_user(user: schemas.UserCreate,db: Session=Depends(database.get_db)):
    db_user=crud.get_user_by_email(db,email=user.email)
    if db_user:
        raise HttpException(status_code=400, detail="email already registered")
    hashed_password=auth.get_password_hash(user.password)
    user.password=hashed_password
    return crud.create_user(db=db, user=user)

@router.post("/login/", response_model=schemas.Token)
def login_user(form_data: OAuth2PasswordRequestForm=Depends(), db:Session=Dependsd(database.get_db)):
    user=auth.authenticate_user(db,form_data.username, form_data.password)
    if not user:
        raise HttpException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Autheticate": "Bearer"},
        )
    access_token=auth.create_access_token(data={"sub": str(user.id)})
    return {"access_token": access_token,"token_type":"bearer"}

@router.get("/me/", response_model=schemas.UserReponse)
def read_user_me(current_user:schemas.UserResponse=Depends(auth.get_current_user)):
    return current_user
