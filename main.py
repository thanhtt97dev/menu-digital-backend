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
# 1. Create a Virtual Enviroment:
#   python -m venv venv
#
# 2. Install libs
#   pip install -r requirements.txt
#
# 3. Docker:
#   docker-compose up -d
#
# 4. Migration database with Alembic: 
# 4.1. Add new migration:
#   alembic revision --autogenerate -m "message"
# 4.2. Update database  
#   alembic upgrade head:
# 
# 5. Run app:
#   uvicorn main:app --reload
