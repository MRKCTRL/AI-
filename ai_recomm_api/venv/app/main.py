from fastapi import FASTAPI
from .routers import users, content, recommendations 
from .database import Base, engine 
from fastapi import FASTAPI,WebSocket

Base.metadata.create_all(bind=engine)


app= FASTAPI()


app.include_router(users.router.router,prefix="/api/v1")
app.include_router(content.router,prefix="/api/v1")
app.include_router(recommendations.router,prefix="/api/v1")


async.websocket("/ws")
async def websocket_endpoint(websocket:WebSocket):
    await websocket.accept()
    while True:
        data=await websocket.recieve_text()
        await websocket.send_text(f"Message recieved: {data}")