from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    __tablename__="users"
    id=Column(Integer,Primary_key=True,Index=True)
    email=Column(String, unique=True,index=True)
    password=Column(String)
    
    
    interactions=relationship("Interaction", back_populate="user")
    

class Content(Base):
    __tablename__="content"
    id=Column(Integer,primary_key=True, index=True)
    title=Column(String,index=True)
    description=Column(String)
    type=Column(String)
    
    interactions=relationship("Interactions", back_populate="content")
    
class Interaction(Base):
    __tablename__="interactions"
    id=Column(Integer, primary_key=True,index=True)
    user_id=Column(Integer, ForeignKey("user.id"))
    content_id=Column(Integer,ForeignKey("content.id"))
    rating=Column(Float)
    timestamp=Column( Datetime, default=func.now())
    
    
    user=relationship("User", back_populates="interactions")
    content=relationship("content", back_populates="interactions")
    