import celery import Celery


celery_app=Celery("tasks", broker="redis://localhost:6379/0")

@celery_app.task
def train_recommendation_model():
    pass