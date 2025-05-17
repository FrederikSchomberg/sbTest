from fastapi import FastAPI, HTTPException
from datetime import datetime, UTC
from typing import List
from models import User, StudyGroupCreate, StudyGroup

app = FastAPI(title="Study Buddy Mock API")

# Mock data
mock_users = [
    User(id=1, name="John Doe", email="john@example.com", created_at=datetime.now(UTC)),
    User(id=2, name="Jane Smith", email="jane@example.com", created_at=datetime.now(UTC)),
    User(id=3, name="Alice Johnson", email="alice@example.com", created_at=datetime.now(UTC)),
]
mock_study_groups: List[StudyGroup] = []

def get_study_group_id() -> int:
    return len(mock_study_groups) + 1

# New Root Endpoint: Welcome message
@app.get("/")
async def root():
    """Welcome message for StudyBuddy API."""
    return {"message": "Welcome to StudyBuddy"}

# Use Case 1: GET all users
@app.get("/users/", response_model=List[User])
async def get_users():
    """Retrieve all users."""
    return mock_users

# Use Case 2: GET user by ID
@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    """Retrieve a user by ID."""
    if user_id <= 0:
        raise HTTPException(status_code=400, detail="Invalid user ID")
    for user in mock_users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

# Use Case 3: POST create study group
@app.post("/study_groups/", response_model=StudyGroup, status_code=201)
async def create_study_group(group: StudyGroupCreate):
    """Create a new study group."""
    new_id = get_study_group_id()
    new_group = StudyGroup(
        id=new_id,
        created_at=datetime.now(UTC),
        **group.dict()
    )
    mock_study_groups.append(new_group)
    return new_group