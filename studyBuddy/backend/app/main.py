from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .mock_data import users, groups, meetings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to StudyBuddy API"}

@app.get("/users")
def list_users():
    return users

@app.get("/groups")
def list_groups():
    return groups

@app.post("/groups/join/{group_id}")
def join_group(group_id: int):
    for group in groups:
        if group["id"] == group_id:
            group["members"] += 1
            return {"message": f"Joined group {group_id}"}
    raise HTTPException(status_code=404, detail="Group not found")

@app.get("/meetings")
def list_meetings():
    return meetings

@app.post("/meetings")
def create_meeting(meeting: dict):
    meetings.append(meeting)
    return {"message": "Meeting created", "data": meeting}
