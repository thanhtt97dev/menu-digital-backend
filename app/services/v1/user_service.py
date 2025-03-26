from sqlalchemy.orm import Session
from sqlalchemy import select, or_

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.common.shared.responses.response import Response
from app.schemas.user_schema import UserSchema

class UserService():
    
    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)
        
    def get_users(self, search: str, page_index: int, page_size: int):
        query = self.user_repository.get_users(search)
        results = self.user_repository.get_paginated(query, page_index, page_size)
        
        users = [UserSchema.from_orm(user) for user in results['items']]
        
        results = {
            **results,
            'items' : users
        }
        
        return Response.success(results)

    