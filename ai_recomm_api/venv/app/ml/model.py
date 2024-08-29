import pickle 
import numpy as np 
from ..models import Interaction
 
class InteractionMatrix:
    def __int__(self, interactions):
        self.user_ids=sorted(list(set([interaction.user_id for interaction in interactions]))) 
        self.content_ids=sorted(list(set([interaction.content_id for interaction in interactions]))) 
        self.matrix=np.zeros((len(self.user_ids), len(self.content_ids)))
        
        for interaction in interactions:
            user_idx=self.user_ids.index(interaction.user_id)
            content_idx=self.content_ids.index(interaction.content_id)
            self.matrix[user_idx][content_idx] =interaction.rating
            
    
    def get_recommendations(user_id: int):
        with open("app/ml/recommendation_model/pkl", "rb") as f:
            model=pickle.load(f)
            
        user_idx=InteractionMatrix.user_ids.index(user_id)
        distances, indices= model.kneighbors([InteractionMatrix.matrix[user_idx]])0
        
        recommended_content_ids=[InteractionMatrix.content_ids[i]for i in indices[0]]
        return recommended_content_ids
     
            