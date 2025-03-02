from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.common.Shared.Configurations.enviroment_config import settings

# make engine connect with MySql
engine = create_engine(settings.DATABASE_URL)

# create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base Model
Base = declarative_base()

# Dependency get session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()