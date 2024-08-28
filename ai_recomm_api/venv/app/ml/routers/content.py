from fastapi import APIRouter, Depends, HTTPException 
from sqlalchemy.orm import Session 
from .. import schemas, crud, database

router=APIRouter()

@router.post("/content/", response_model=schemas.Cotent)
def create_content(content:schemas.ContentCreate, db:Session=Depends(database.get_db)):
    return crud.create_content(db=db, content=content)

@