from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.common.shared.configurations.enviroment_config import enviroment

def cors_middleware(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[enviroment.ALLOWED_ORIGIN],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    