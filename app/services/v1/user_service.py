from sqlalchemy.orm import Session
from sqlalchemy import select, or_

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.common.shared.responses.response import Response
from app.schemas.user_schema import UserSchema, UserUpdateStatus

class UserService():
    
    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)
        
    def get_users(self, username: str, fullname: str, email: str, role_id: int, status_id: int, page_index: int, page_size: int):
        query = self.user_repository.get_users(username, fullname, email, role_id, status_id)
        results = self.user_repository.get_paginated(query, page_index, page_size)
        
        users = [UserSchema.from_orm(user) for user in results['items']]
        
        results = {
            **results,
            'items' : users
        }
        
        return Response.success(results)
    
    def update_user_status(self,user_id: str, user_data: UserUpdateStatus):
        self.user_repository.update(user_id, user_data.__dict__)
        return Response.success()

    