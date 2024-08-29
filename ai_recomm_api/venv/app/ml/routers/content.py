from fastapi import APIRouter, Depends, HTTPException 
from sqlalchemy.orm import Session 
from .. import schemas, crud, database

router=APIRouter()

@router.post("/content/", response_model=schemas.Cotent)
def create_content(content:schemas.ContentCreate, db:Session=Depends(database.get_db)):
    return crud.create_content(db=db, content=content)

@router.get("/content/{content_id}", response_model=schemas.ContentResponse)
def get_content(content_id:int,db:Session=Depends(database.get_db)):
    db_content=crud.get_content(db, content_id=content_id)
    if db_content is None:
        raise HTTPException(status_code=404, detail="Content ot found")
    return db_content