import uvicorn
from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI

from app.common.shared.configurations.routers_config import include_routers
from app.common.shared.configurations.middlewares_config import include_middlewares

app = FastAPI()

# include routers
include_routers(app)

# api versioning
app = VersionedFastAPI(app, version_format="{major}", prefix_format="/api/v{major}")

# include middlewares
include_middlewares(app)

@app.on_event("startup")
async def on_startup():
    pass

if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)
    

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
# 4.1. Update [sqlalchemy.url] in [alembic.ini]:
#   sqlalchemy.url = mysql+pymysql://root:sa@localhost:3306/menu-digital
# 4.2. Add new empty database
# 4.2. Add new migration:
#   alembic revision --autogenerate -m "message"
# 4.3. Update database  
#   alembic upgrade head
# 
# 5. Run app:
#   uvicorn main:app --reload
