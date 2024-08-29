from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 
from ..ml.model import get_recommendations
from .. import database, crud, schemas 

router=APIRouter()

@router.get("/recommendations/{user_id}", response_model=List[schemas.ContentResponse])
def recommend_content(user_id:int, db: Session=Depends(database.get_db)):
    recommend_content_ids=get_recommendations(user_id)
    recommendations=[crud.get(db, content_id) for content_id in recommend_content_ids]
    
    
    return recommendations