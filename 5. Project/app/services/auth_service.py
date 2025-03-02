from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.models.user import User
from app.schemas.auth_schema import SignUp

class AuthService():
    
    def __init__(self, db):
        self.user_repository = UserRepository(db)
    
    def sign_up(self, sign_up_data: SignUp):
        is_username_existed = self.user_repository.get_user_by_username(sign_up_data.username)
        if (is_username_existed):
            raise Exception()
        
        user_db = User(
            username = sign_up_data.username,
            email = 'test',
            hashed_password= sign_up_data.password,
            role_id = 1
        )
        
        user = self.user_repository.add(user_db)
        user.hashed_password = ''
        return user