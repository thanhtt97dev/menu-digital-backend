from fastapi import APIRouter, Depends
from fastapi_versioning import version
from sqlalchemy.orm import Session


from app.db.database import get_db
from app.services.v1.auth_service import AuthService
from app.schemas.auth_schema import (
    SignUp,
    SignIn,
    SignInByGoogle
)
from app.common.shared.configurations.enviroment_config import enviroment

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/signup")
@version(enviroment.API_VERSION)
def sign_up(sign_up_data: SignUp, db: Session = Depends(get_db)):
    return AuthService(db).sign_up(sign_up_data)
    
    
@router.post('/signin')
@version(enviroment.API_VERSION)
def sign_in(sign_data: SignIn, db: Session = Depends(get_db)):
    return AuthService(db).sign_in(sign_data)

@router.post('/SignInByGoogle')
@version(enviroment.API_VERSION)
def sign_in_by_google(sign_in_google_data: SignInByGoogle, db: Session = Depends(get_db)):
    return AuthService(db).sign_in_by_google(sign_in_google_data)