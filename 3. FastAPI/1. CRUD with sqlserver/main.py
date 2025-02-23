from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import database
from models import user
from pydantic import BaseModel

app = FastAPI()

# Dependency để lấy database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Schema dùng Pydantic
class UserCreate(BaseModel):
    name: str
    email: str

class UserResponse(UserCreate):
    id: int

# API: Thêm user
@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = user.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# API: Lấy danh sách user
@app.get("/users/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return db.query(user.User).all()
