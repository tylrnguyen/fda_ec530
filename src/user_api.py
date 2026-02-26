from fastapi import FastAPI, HTTPException, Query
from typing_extensions import Annotated, List, Dict
from pydantic import BaseModel, Field
import requests


app = FastAPI()


class User(BaseModel):
    username: str = Field(
        min_length = 1,
        max_length = 100,
        description = "Name of the user"
    )
    id: int
    notes: List[str] = Field(default_factory=list, description = "User's text notes")
   
users_db: Dict[int, User] = {}

num_users = 0 # Used for id

# Returns welcome message
@app.get("/")
def home():
    return {"message": "Welcome to the user API"}

# Returns list of users
@app.get("/users")
def get_users():
    return users_db

# Returns user's id
@app.get("/users/{id}")
def get_account(id: int):
    if id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return {
        "username": users_db[id]
    }

# Returns user's notes
@app.get("/users/{id}/notes")
def get_notes(id: int):
    if id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[id].notes

# Adds a user
@app.post("/users")
def add_user(username: str):
    global num_users
    if any(u.username == username for u in users_db.values()):
        HTTPException(status_code=409, detail="Username already in database")
    user = User(username=username,id=num_users)
    users_db[num_users] = user
    num_users += 1
    return {"message": "User added successfully", "user": user}

# Adds a note to user's notes
@app.post("/users/{id}/notes")
def add_note(id: int, text_note: str):
    if id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    users_db[id].notes.append(text_note)
    return {
        "message": f"Note added to user {id} successfully",
        "user": users_db[id].username,
        "note": text_note
    }

# Adds random drug event to user's notes
@app.post("/users/{id}/notes/event")
def add_event(id: int):
    if id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    r = requests.get(f'https://api.fda.gov/drug/event.json')
    users_db[id].notes.append(r.text)
    return {
        "message": f"Note added to user {id} successfully",
        "user": users_db[id].username,
        "note": r.text
    }

# Adds random drug label to user's notes
@app.post("/users/{id}/notes/label")
def add_event(id: int):
    if id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    r = requests.get(f'https://api.fda.gov/drug/label.json')
    users_db[id].notes.append(r.text)
    return {
        "message": f"Note added to user {id} successfully",
        "user": users_db[id].username,
        "note": r.text
    }

# Adds random drug enforcement event to user's notes
@app.post("/users/{id}/notes/enforcement")
def add_event(id: int):
    if id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    r = requests.get(f'https://api.fda.gov/drug/enforcement.json')
    users_db[id].notes.append(r.text)
    return {
        "message": f"Note added to user {id} successfully",
        "user": users_db[id].username,
        "note": r.text
    }


   

