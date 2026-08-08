from fastapi import APIRouter
from app.schemas.user_schema import UserCreate

router = APIRouter()

@router.post("/signup")
def signup(user: UserCreate):
    return {
        "name": user.name,
        "email": user.email,
        "message": "User registered successfully"
    }