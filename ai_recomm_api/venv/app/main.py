from fastapi import FASTAPI
from .routers import users, content, recommendations 
from .database import Base, engine 


Base.metadata.create_all(bind=engine)


app= FASTAPI()


app.include_router(users.router.router,prefix="/api/v1")
app.include_router(content.router,prefix="/api/v1")
app.include_router(recommendations.router,prefix="/api/v1")
