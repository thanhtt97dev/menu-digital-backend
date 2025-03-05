from typing import Tuple
from fastapi import status
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

from app.common.shared.responses.base_response import BaseResponse
from app.common.shared.exceptions.base.bad_request_exeption import BadRequestException
from app.common.shared.exceptions.base.domain_exception import DomainException

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
                return status.HTTP_400_BAD_REQUEST, BaseResponse.failure(exception.message).__dict__
            case _:
                return status.HTTP_500_INTERNAL_SERVER_ERROR, BaseResponse.failure().__dict__