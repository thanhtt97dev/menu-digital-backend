from sqlalchemy import select, Select
from sqlalchemy.orm import Session, Query
from typing import Generic, TypeVar, Type, Tuple, Any
from app.db.database import Base
from math import ceil
from common.shared.constants.app_constant import AppConstants

T = TypeVar("T", bound=Base)

class BaseRepository(Generic[T]):
    
    def __init__(self, model: Type[T], db: Session):
        self.model = model
        self.db = db
        
    def get_by_id(seft, id: any) -> T | None:
        return seft.db.query(seft.model).filter(seft.model.id == id).first()
    
    def get_all(self) -> list[T]:
        return self.db.query(self.model).all()
    
    def get_paginated(self, query: Query[T], page: int = AppConstants.Page.INDEX_DEFAULT, page_size: int = AppConstants.Page.SIZE_DEFAULT):
        total_count = query.count()
        total_pages = ceil(total_count / page_size)
        results = query.offset((page - 1) * page_size).limit(page_size).all()
        return {
            "total_count": total_count,
            "total_pages": total_pages,
            "current_page": page,
            "page_size": page_size,
            "data": results
        }
    
    def create(self, db_data: dict) -> T:
        db_obj = self.model(**db_data)
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj
    
    def update(self, db_obj: T, update_data: dict) -> T:
        for key, value in update_data.items():
            setattr(db_obj, key, value)
            
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj
    
    def delete(self, id) -> bool:
        obj = self.get_by_id(id)
        if (not obj):
            return False
        self.db.delete(obj)
        self.db.commit()
        
    def execute(self, query: Select[Tuple[Any, ...]]):
        return self.db.execute(query)
