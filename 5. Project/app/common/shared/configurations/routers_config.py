from fastapi import FastAPI
from app.routers import (
    role_route,
    user_route,
    auth_route,
)

def include_routers(app: FastAPI):
    app.include_router(user_route.router)
    app.include_router(role_route.router)
    app.include_router(auth_route.router)