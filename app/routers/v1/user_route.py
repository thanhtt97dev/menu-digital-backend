from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Optional

from app.db.database import get_db
from app.services.v1.user_service import UserService
from app.schemas.user_schema import UserCreate, UserResponse
from app.common.shared.constants.app_constant import AppConstants


router = APIRouter(prefix="/users", tags=["Users"])

@router.get("")
def get_users(
    search: Optional[str] = '' , 
    page_index: int = AppConstants.Page.INDEX_DEFAULT, 
    page_size: int  = AppConstants.Page.SIZE_DEFAULT,
    db: Session = Depends(get_db)
):
    return UserService(db).get_users(search, page_index, page_size)