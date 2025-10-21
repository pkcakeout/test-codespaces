from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.post("/items/")
async def create_item(item: dict):
    return {"item": item}

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}

@app.post("/users/")
async def create_user(user: dict):
    return {"user": user}

client = TestClient(app)

def test_read_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1}

def test_create_item():
    response = client.post("/items/", json={"name": "test item"})
    assert response.status_code == 200
    assert response.json() == {"item": {"name": "test item"}}

def test_read_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == {"user_id": 1}

def test_create_user():
    response = client.post("/users/", json={"name": "test user"})
    assert response.status_code == 200
    assert response.json() == {"user": {"name": "test user"}}