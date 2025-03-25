from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.user_schema import UserCreate, UserResponse

from app.services.v1.user_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("")
def get_users(db: Session = Depends(get_db)):
    return UserService(db).get_users()