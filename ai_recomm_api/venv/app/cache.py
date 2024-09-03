import redis 
import fastapi import Depends
import json
import requests 

redis_client=redis.Redis(host='localhost', port='6379', db='0')

def cash_response(key:str, response:dict, expiration:int=60):
    redis_client.set(key, json.dumps(response), ex=expiration)
    
    
def get_cached_response(key:str):
    data=redis_client.get(key)
    return json.loads(data) if data else None
