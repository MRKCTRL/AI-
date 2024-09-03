from fastapi.testclient import TestClient
from app.main import app

client=TestClient(app)


def test_readu_main():
    response =client.get("/api/v1/content")
    assert response.status_code==200
    assert response.json() =={"message": "hello world"}