from typing import Type, TypeVar, Generic
from sqlalchemy.orm import Session

T = TypeVar('T')

class BaseRepository(Generic[T]):
    """Clase base para todos los repositorios"""
    def __init__(self, model: Type[T], db: Session):
        self.model = model
        self.db = db

    def get(self, id: str) -> T:
        return self.db.query(self.model).filter(self.model.id == id).first()

    def create(self, obj: T) -> T:
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def update(self, id: str, update_data: dict) -> T:
        obj = self.db.query(self.model).filter(self.model.id == id).first()
        if not obj:
            return None
        
        for key, value in update_data.items():
            setattr(obj, key, value)
        
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def delete(self, id: str) -> bool:
        obj = self.db.query(self.model).filter(self.model.id == id).first()
        if not obj:
            return False
        
        self.db.delete(obj)
        self.db.commit()
        return True