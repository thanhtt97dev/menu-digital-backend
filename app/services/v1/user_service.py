from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.common.shared.responses.response import Response
from app.schemas.user_schema import UserSchema

class UserService():
    
    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)
        
    def get_users(self):
        query = select(User)
        users = self.user_repository.execute(query).scalars().all()
        
        response = [UserSchema.from_orm(user) for user in users]
        return Response.success(response)

    