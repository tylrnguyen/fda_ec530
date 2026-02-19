from fastapi import FastAPI, HTTPException, Query
from typing_extensions import Annotated

app = FastAPI()

users_db = {}

num_users = 0

@app.get("/")
def home():
    return {"message": "Welcome to the user API"}

@app.get("/users/{id}")
def get_account(id: int):
    return {
        "username": users_db[id]
    }

@app.post("/users")
def add_user(username: str):
    global num_users
    if not username:
        raise HTTPException(status_code=400, detail="'username' field is required")
    
    if username in users_db.values():
        raise HTTPException(status_code=409, detail="User already exists")
    
    users_db[num_users] = username
    num_users += 1
    return {"message": "User added successfully", "user": username, "id": (num_users-1)}
