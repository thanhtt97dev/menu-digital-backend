from typing import Tuple
from fastapi import status
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

from app.common.shared.responses.base_response import BaseResponse
from app.common.shared.responses.response import Response
from app.common.shared.exceptions.base.bad_request_exception import BadRequestException
from app.common.shared.exceptions.base.not_found_exception import NotFoundException
from app.common.shared.exceptions.base.un_authorized_exception import UnAuthorizedException
from app.common.shared.exceptions.base.un_authentication_exception import UnAuthenticationException

class ExceptionHandlingMiddleware(BaseHTTPMiddleware):
    
    async def dispatch(self, request, call_next):
        try:
            return await call_next(request)
        except Exception as ex:
            status_code, response = self.get_response_exception(ex)
            return JSONResponse(
                content=response,
                status_code=status_code,
            )

    @staticmethod
    def get_response_exception(exception: Exception) -> Tuple[int, dict]:
        match exception:
            case BadRequestException():
                return status.HTTP_400_BAD_REQUEST, Response.failure(exception.__dict__).__dict__
            case NotFoundException():
                return status.HTTP_404_NOT_FOUND, Response.not_found(exception.__dict__).__dict__
            case UnAuthorizedException():
                return status.HTTP_401_UNAUTHORIZED, Response.un_authorized(exception.__dict__).__dict__
            case UnAuthenticationException():
                return status.HTTP_403_FORBIDDEN, Response.un_authentication(exception.__dict__).__dict__
            case _:
                return status.HTTP_500_INTERNAL_SERVER_ERROR, BaseResponse.failure().__dict__