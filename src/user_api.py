from fastapi import FastAPI, HTTPException, Query
from typing import Annotated

app = FastAPI()

users_db = []

@app.get("/")
def home():
    return {"message": "Welcome to the user API"}

@app.get("/users/{id}")
def get_account(id: int):
    return {
        "username": id
    }

@app.post("/users")
def add_user(username: str):
    if not username:
        raise HTTPException(status_code=400, detail="'username' field is required")
    
    if username in users_db:
        raise HTTPException(status_code=409, detail="User already exists")
    
    users_db.append(username)
    return {"message": "User added successfully", "user": username}
