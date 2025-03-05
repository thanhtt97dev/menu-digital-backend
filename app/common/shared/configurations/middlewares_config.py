from fastapi import FastAPI

from app.middlewares.exception_handling_middleware import ExceptionHandlingMiddleware

def include_middlewares (app: FastAPI):
    
    app.add_middleware(ExceptionHandlingMiddleware)