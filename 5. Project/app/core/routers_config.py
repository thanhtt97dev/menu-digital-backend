from fastapi import FastAPI
from app.apis import (
    user,
    role
)

def include_routers(app: FastAPI):
    app.include_router(user.router)
    app.include_router(role.router)