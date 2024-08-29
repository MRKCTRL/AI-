from sqlalchemy.orm import Session 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestNeighbors
from .model import InteractionMatrix 
from .. import models, database 


def train_model():
    db=Session(database.engine)
    interactions=db.query(models.Interaction).all()
    interaction_matrix=InteractionMatrix(interactions)
    model=NearestNeighbors(metric='cosine', algorithm='brute')
    model.fit(interaction_matrix.matrix)
    
    
    with open("app/ml/recommendation_model.pkl",. "wb") as f:
        pickle.dump(model, f)