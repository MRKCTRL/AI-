from pydantic import BaseModel
from typing import List,Optional
from datetime import datetime

class UserCreate(BaseModel):
    email:str
    descrition:str
    
class ContentCreate(BaseModel):
    title:str 
    description:str
    type:str


class InteractinCreate(BaseModel):
    user_id:int
    content_id:int 
    rating:float
    
class UserResponse(BaseModel):
    id:int
    email:str 
    
    class config:
        orm_mode=True
    
class ContentResponse(BaseModel):
    id:int
    title:str
    description:str 
    type:str
    
    class config:
        orm_mode=True
        
class Token(BaseModel):
    access_token:str
    token_type:str