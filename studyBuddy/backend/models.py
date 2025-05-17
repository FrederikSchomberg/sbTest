from pydantic import BaseModel
from typing import List
from datetime import datetime

class User(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime

class StudyGroupCreate(BaseModel):
    name: str
    description: str
    creator_id: int
    tags: List[str]

class StudyGroup(StudyGroupCreate):
    id: int
    created_at: datetime