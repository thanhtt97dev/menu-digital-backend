import uvicorn
from fastapi import FastAPI
from app.db.database import engine, Base
from app.common.shared.configurations.routers_config import include_routers

app = FastAPI()

# regist routers
include_routers(app=app)


@app.on_event("startup")
async def on_startup():
    pass

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
    

#Note: run command
# Docker: docker-compose up -d
# Alembic: 
#   alembic revision --autogenerate -m "message"
#   alembic upgrade head
# Run app: uvicorn main:app --reload
