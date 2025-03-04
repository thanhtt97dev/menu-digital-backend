
from typing import Generic, TypeVar

from app.common.shared.constants.app_constant import AppConstants

T = TypeVar('T')
class Response(Generic[T]):
    
    def __init__(self, code, message, data: T):
        self.code = code
        self.message = message
        self.data = data

    @staticmethod
    def success(data: T, message: str = "Success!"):
        return Response(AppConstants.ResponseCode.SUCCESS, message, data)
    
    @staticmethod    
    def failure(data: T, message: str = "Failure!"):
        return Response(AppConstants.ResponseCode.FAILURE, message, data)
    
    @staticmethod
    def not_found(data: T, message: str = "Not Found!"):
        return Response(AppConstants.ResponseCode.NOT_FOUND, message, data)
    
    @staticmethod
    def validation_error(data: T, message: str = "Validation error!"):
        return Response(AppConstants.ResponseCode.VALIDATION_ERROR, message, data)
    
    @staticmethod
    def un_authorized(data: T, message: str = "Un authorized!"):
        return Response(AppConstants.ResponseCode.UN_AUTHORIZED, message, data)
    
    @staticmethod
    def un_authentication(data: T, message: str = "Un authentication!"):
        return Response(AppConstants.ResponseCode.UN_AUTHENTICATION, message, data)
    
    @staticmethod
    def initialization(code: str, message: str | None, data: T):
        return Response(code, message, data)
