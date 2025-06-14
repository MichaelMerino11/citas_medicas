from pydantic import BaseModel
from datetime import datetime

class BaseSchema(BaseModel):
    """Esquema base para todos los modelos"""
    class Config:
        from_attributes = True  # Equivalente a orm_mode en Pydantic v1
        json_encoders = {
            datetime: lambda v: v.isoformat()  # Formato para datetime
        }