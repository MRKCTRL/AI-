from sqlalchemy.orm import Session 
from . import models, schemas

def create_user(db: Session, user:schemas.UserCreate):
    db_user=models.User(email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_content(db:Session, content: schemas.ContentCreate):
    db_content=models.Content(title=content.title, description=content.description, type=content.type)
    db.addd(db_content)
    db.commit()
    db.refresh(db_content)
    return db_content


def create_interaction(db:Session, interaction:schemas.InteractinCreate):
    db_interaction=models.Interaction(user_id=interaction.user_id, content_id=interaction.content_id,rating=interaction.rating)
    db.add(db_interaction)
    db.commmit()
    db.refresh(db_interaction)
    return db_interaction


def get_user(db:Session, user_id:int):
    return db.query(models.User).filter(models.User.id ==user_id).first()

def get_content(db: Session, content_id:int):
    return db.query(models.Content).filter(models.Content.id == content_id).frst()

def get_interactions(db:Session, user_id:int):
    return db.query(models.Interaction).filter(models.Interaction.user_id ==user_id).all()

def get_user_by_email(db: Session, email:str):
    return db.query(models.User).filter(models.User.email==email)
