import uuid
from sqlalchemy import select
from google.auth.transport import requests
from google.oauth2 import id_token

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.common.shared.responses.response import Response
from app.schemas.auth_schema import (
    SignUp,
    SignIn,
    SignInByGoogle,
)
from app.common.shared.responses.response import Response
from app.common.shared.exceptions.base.un_authorized_exception import UnAuthorizedException
from app.common.shared.constants.app_constant import AppConstants
from app.extenal_services.jwt_service import JwtService

class AuthService():
    
    def __init__(self, db, jwt_service: JwtService = JwtService()):
        self.user_repository = UserRepository(db)
        self.jwt_service = jwt_service
    
    def sign_up(self, sign_up_data: SignUp):
        is_username_existed = self.user_repository.get_user_by_username(sign_up_data.username)
        if (is_username_existed):
            raise Response.failure('Username has been exsited!')
        
        user_db = User(
            id = str(uuid.uuid4()),
            username = sign_up_data.username,
            password = sign_up_data.password,
            fullname = sign_up_data.fullname,
            email = sign_up_data.email,
            role_id = AppConstants.Role.Employee,
            status = AppConstants.User.Status.UnActivate
        )
        
        user = self.user_repository.add(user_db)
        user.password = ''
        return Response.success(user)
    
    def sign_in(self, sign_in_data: SignIn):
        query = (
            select(User)
            .where(
                User.username == sign_in_data.username and 
                User.password == sign_in_data.password
            )
        )
        
        user = self.user_repository.execute_scalar_one_or_none(query)
        
        if user is None:
            return Response.not_found('Username or Password incorrect!')
        
        if user.status == AppConstants.User.Status.Deactivate:
            raise UnAuthorizedException(title=None, content='Your account has ben banned!')
        
        payload = {
                'id' : user.id,
                'role': user.role_id,
                'username': user.username,
                'email': user.email
            }
        
        token = self.jwt_service.generate_token(payload)
        
        return Response.success({'accessToken': token, 'userId': user.id})
        
    def sign_in_by_google(self, sign_in_by_google_data: SignInByGoogle):
        id_info = id_token.verify_oauth2_token(sign_in_by_google_data.googleToken, requests.Request())
        
        user_info = User(email=id_info['email'], fullname=id_info['name'])      
        # check user is registed
        query_check_user_registed = (
            select(User)
            .where(User.email == user_info.email)
        )
        user = self.user_repository.execute_scalar_one_or_none(query_check_user_registed)
        
        if user is not None:
            if user.status == AppConstants.User.Status.UnActivate:
                raise UnAuthorizedException('Your account is not activeted!')
            if user.status == AppConstants.User.Status.Deactivate:
                raise UnAuthorizedException('Your account is banned!')
            else :
                return self.sign_in_response(user)
        else:
            user_db = User(
                id = str(uuid.uuid4()),
                fullname = user_info.fullname,
                email = user_info.email,
                role_id = AppConstants.Role.Employee,
                status = AppConstants.User.Status.Activate
            )
            user = self.user_repository.add(user_db)
            return self.sign_in_response(user)
    
    def sign_in_response(self, user: User):
        payload = {
                'id' : user.id,
                'role': user.role_id,
                'username': user.username,
                'email': user.email
            }
        token = self.jwt_service.generate_token(payload)
        return Response.success({'accessToken': token, 'refreshToken': '', 'userId': user.id})