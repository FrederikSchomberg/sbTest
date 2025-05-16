import pytest
from httpx import AsyncClient
from main import app


@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp = await ac.get("/")
        assert resp.status_code == 200
        assert resp.json()["message"] == "Welcome to StudyBuddy API"

@pytest.mark.asyncio
async def test_users():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp = await ac.get("/users")
        assert resp.status_code == 200
        assert isinstance(resp.json(), list)

@pytest.mark.asyncio
async def test_groups_and_join():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp = await ac.get("/groups")
        assert resp.status_code == 200
        groups = resp.json()
        assert len(groups) > 0
        group_id = groups[0]["id"]

        resp = await ac.post(f"/groups/join/{group_id}")
        assert resp.status_code == 200
        assert "Joined group" in resp.json()["message"]
