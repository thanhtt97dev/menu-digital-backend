from typing import Generic, TypeVar

from app.common.shared.constants.app_constant import AppConstants
from app.common.shared.responses.base_response import BaseResponse

T = TypeVar('T')
class Response(Generic[T], BaseResponse):
    
    def __init__(self, code, message, data: T):
        super().__init__(code, message)
        self.data = data

    @staticmethod
    def success(data: T):
        return Response(AppConstants.ResponseCode.SUCCESS, "Success!", data)
    
    @staticmethod    
    def failure(data: T):
        return Response(AppConstants.ResponseCode.FAILURE, "Failure!", data)
    
    @staticmethod
    def not_found(data: T):
        return Response(AppConstants.ResponseCode.NOT_FOUND, "Not Found!", data)
    
    @staticmethod
    def validation_error(data: T):
        return Response(AppConstants.ResponseCode.VALIDATION_ERROR, "Validation error!", data)
    
    @staticmethod
    def un_authorized(data: T):
        return Response(AppConstants.ResponseCode.UN_AUTHORIZED, "Un authorized!", data)
    
    @staticmethod
    def un_authentication(data: T):
        return Response(AppConstants.ResponseCode.UN_AUTHENTICATION, "Un authentication!", data)
