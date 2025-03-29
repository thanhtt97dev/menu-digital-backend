from sqlalchemy import func, select, Select
from sqlalchemy.orm import Session, Query
from typing import Generic, TypeVar, Type, Tuple, Any
from app.db.database import Base
from math import ceil
from app.common.shared.constants.app_constant import AppConstants

T = TypeVar("T", bound=Base)

class BaseRepository(Generic[T]):
    
    def __init__(self, model: Type[T], db: Session):
        self.model = model
        self.db = db
        
    def get_by_id(seft, id: any) -> T | None:
        return seft.db.query(seft.model).filter(seft.model.id == id).first()
    
    def get_all(self) -> list[T]:
        return self.db.query(self.model).all()
    
    def get_paginated(self, query: Select, page_index: int = AppConstants.Page.INDEX_DEFAULT, page_size: int = AppConstants.Page.SIZE_DEFAULT):
        # Count total records
        total_count_query = select(func.count()).select_from(query.subquery())
        total_count = self.db.execute(total_count_query).scalar_one()
        
        # Get total page
        total_pages = ceil(total_count / page_size)
        
        # Update page_index
        if (page_index <= 0):
            page_index = AppConstants.Page.INDEX_DEFAULT
        
        if (page_index > total_pages):
            page_index = total_pages

        # Apply pagination to the original query
        paginated_query = query.offset((page_index - 1) * page_size).limit(page_size)
        items = self.db.execute(paginated_query).all()
        
        return {
            "totalCount": total_count,
            "totalPages": total_pages,
            "pageIndex": page_index,
            "pageSize": page_size,
            "hasNextPage": page_index * page_size < total_count,
            "hasPreviousPage": page_index > 1,
            "items": items
        }
    
    def add(self, db_data) -> T:
        self.db.add(db_data)
        self.db.commit()
        self.db.refresh(db_data)
        return db_data
    
    def update(self, obj_id: int, update_data: dict) -> T:
        db_obj = self.get_by_id(obj_id)
        if not db_obj:
            return None

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
    
    def execute_scalar_one_or_none(self, query: Select[Tuple[Any, ...]]):
        return self.db.execute(query).scalar_one_or_none()
