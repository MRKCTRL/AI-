from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session 
from ..ml.model import get_recommendations
from .. import database, crud, schemas 
from ..celery_worker import train_recommendation_model


router=APIRouter()

@router.get("/recommendations/{user_id}", response_model=List[schemas.ContentResponse])
def recommend_content(user_id:int, db: Session=Depends(database.get_db)):
    recommend_content_ids=get_recommendations(user_id)
    recommendations=[crud.get(db, content_id) for content_id in recommend_content_ids]
    
    
    return recommendations

@router.post("/train-model/")
def train_model(background_tasks:BackgroundTasks):
    background_tasks.add_tasks(train_recommendation_model)
    return {"status":"Model training startedin the background"}