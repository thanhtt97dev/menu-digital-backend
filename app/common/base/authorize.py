
from fastapi import Depends, Request
from fastapi.security import OAuth2PasswordBearer


from app.common.shared.constants.app_constant import AppConstants
from app.extenal_services.jwt_service import JwtService, get_jwt_service
from app.common.shared.exceptions.base.un_authorized_exception import UnAuthorizedException
from app.schemas.auth_schema import UserModel

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/signin")

def authorize(required_roles: list[str] = None):
    def verify_token(request: Request, token: str = Depends(oauth2_scheme), jwtService: JwtService = Depends(get_jwt_service)):
        user_data = jwtService.verify_token(token)
        user = UserModel(**user_data)
                
        if required_roles and user.role not in required_roles:
            raise UnAuthorizedException('Access denied')
        
        user_id_request = request.path_params.get("id")
        if (user.role != AppConstants.Role.Admin and user_id_request is not None and user_id_request != user.id):
            raise UnAuthorizedException('Access denied')
        
        return user
    
    return verify_token