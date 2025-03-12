from fastapi import APIRouter, Depends
from fastapi_versioning import version
from sqlalchemy.orm import Session


from app.db.database import get_db
from app.services.v1.auth_service import AuthService
from app.schemas.auth_schema import (
    SignUp,
    SignIn
)
from app.common.shared.configurations.enviroment_config import settings

API_VERSION = settings.API_VERSION

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/signup")
@version(API_VERSION)
def sign_up(sign_up_data: SignUp, db: Session = Depends(get_db)):
    return AuthService(db).sign_up(sign_up_data)
    
    
@router.post('/signin')
@version(API_VERSION)
def sign_in(sign_data: SignIn, db: Session = Depends(get_db)):
    return AuthService(db).sign_in(sign_data)