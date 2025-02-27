from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import get_user, create_user

router = APIRouter()

@router.post("/users", response_model=UserResponse)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    if get_user(db, user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db, user)
