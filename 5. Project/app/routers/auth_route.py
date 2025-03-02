from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.auth_schema import SignUp
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/signup")
def sign_up(sign_up_data: SignUp, db: Session = Depends(get_db)):
    user = AuthService(db).sign_up(sign_up_data)
    return user