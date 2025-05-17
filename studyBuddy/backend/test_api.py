import pytest
import httpx
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.mark.asyncio
async def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to StudyBuddy"}

@pytest.mark.asyncio
async def test_get_users():
    response = client.get("/users/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 3
    assert data[0]["name"] == "John Doe"

@pytest.mark.asyncio
async def test_get_user_success():
    response = client.get("/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "John Doe"

@pytest.mark.asyncio
async def test_get_user_not_found():
    response = client.get("/users/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"

@pytest.mark.asyncio
async def test_get_user_invalid_id():
    response = client.get("/users/-1")
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid user ID"

@pytest.mark.asyncio
async def test_create_study_group():
    payload = {
        "name": "Math Study Group",
        "description": "Group for math enthusiasts",
        "creator_id": 1,
        "tags": ["math", "study"]
    }
    response = client.post("/study_groups/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Math Study Group"