import jwt
from datetime import datetime, timedelta

from app.common.abstractions.extenal_services.jwt_service_interface import JwtServiceInterface
from app.common.shared.configurations.enviroment_config import enviroment
from app.common.shared.exceptions.base.un_authentication_exception import UnAuthenticationException


class JwtService(JwtServiceInterface):
    
    def generate_token(self, payload: dict, secret: str = enviroment.JWT_ISSUER_SIGNING_KEY, expires_in: int = enviroment.JWT_EXPIRE_MINUTES, algorithm: str = 'HS256'):
        data = payload.copy()
        expire = datetime.utcnow() + timedelta(minutes=expires_in)
        data.update({"exp": expire})
        return jwt.encode(data, secret, algorithm)
    
    
    def verify_token(self, token: str, secret: str = enviroment.JWT_ISSUER_SIGNING_KEY, algorithm: str = 'HS256'):
        try:
            payload = jwt.decode(
                token,
                secret,
                algorithms=[algorithm],
                issuer= enviroment.JWT_VALID_ISSUER if enviroment.JWT_VALIDATE_ISSUER else None,
                audience= enviroment.JWT_VALID_AUDIENCE if enviroment.JWT_VALIDATE_AUDIENCE else None,
                options={"verify_exp": enviroment.JWT_VALIDATE_LIFETIME},
            )
            return payload
        except jwt.ExpiredSignatureError:
            raise UnAuthenticationException('Token exprired!')
        except jwt.InvalidTokenError:
            raise UnAuthenticationException('Token invalid!')
        
def get_jwt_service():
    return JwtService()

    