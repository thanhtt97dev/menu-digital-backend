from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class PostBase(BaseModel):
    title: str
    content: str
    user_id: int
    
class UserBase(BaseModel):
    username: str
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependency = Annotated[Session, Depends(get_db)]


@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: db_dependency):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    
@app.get("/users", status_code=status.HTTP_200_OK)
async def get_users(db: db_dependency):
    user = db.query(models.User).all()
    if user == None:
        raise HTTPException(status_code=404, detail='user not existed')
        
    return user

@app.get('/users/{user_id}')
async def get_user(user_id: int, db: db_dependency):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user == None:
        raise HTTPException(status_code=404, detail='user not existed')
    return user
    
    
@app.get('/test')
async def get_test(test_id: int, order_by: str, status: bool = None):
    return f"{test_id} {order_by} {status}"


@app.post('/posts', status_code=status.HTTP_201_CREATED)
async def create_post(user_id: int, post: PostBase, db: db_dependency):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if (user == None):
        raise HTTPException(status_code=404, detail='user not found')
    
    post_data = models.Post(**post.dict())
    post_data.user_id = user_id
    db.add(post_data)
    db.commit()
    
    
@app.put('/post/{post_id}',status_code=status.HTTP_200_OK)
async def update_post(post_id:int, post_update: PostBase, db: db_dependency):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if post == None:
        raise HTTPException(status_code=404, detail='post not found')
    
    post.title = post_update.title
    post.content = post.content
    db.commit()
    db.refresh(post)
    return post