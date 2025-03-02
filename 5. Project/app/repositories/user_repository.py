from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.role import Role
from app.schemas.role_schema import RoleCreate


from app.common.abstractions.base_repository import BaseRepository
from app.models.user import User
class UserRepository(BaseRepository[User]):
    
    def __init__(self, db):
        super().__init__(User,db)
        
    def get_user_by_username(self, username: str) -> User | None:
        query = (
            select(User).where(User.username == username)
        )
        result = self.execute_scalar_one_or_none(query)
        return result