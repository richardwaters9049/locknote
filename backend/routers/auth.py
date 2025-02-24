from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db
import bcrypt

router = APIRouter(prefix="/auth", tags=["Auth"])

# In-memory user store (Replace with a database model later)
fake_users_db = {}


# User Schema
class User(BaseModel):
    username: str
    password: str


# Hash Password
def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


# Verify Password
def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())


@router.post("/register")
def register(user: User, db: Session = Depends(get_db)):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed_password = hash_password(user.password)
    fake_users_db[user.username] = hashed_password
    return {"message": "User registered successfully"}


@router.post("/login")
def login(user: User, db: Session = Depends(get_db)):
    if user.username not in fake_users_db:
        raise HTTPException(status_code=400, detail="Invalid username or password")

    hashed_password = fake_users_db[user.username]
    if not verify_password(user.password, hashed_password):
        raise HTTPException(status_code=400, detail="Invalid username or password")

    return {"message": "Login successful"}
