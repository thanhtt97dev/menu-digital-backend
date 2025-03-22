from fastapi import FastAPI

from app.middlewares.exception_handling_middleware import ExceptionHandlingMiddleware
from app.middlewares.cors_middleware import cors_middleware

def include_middlewares (app: FastAPI):
    
    app.add_middleware(ExceptionHandlingMiddleware)
    cors_middleware(app)