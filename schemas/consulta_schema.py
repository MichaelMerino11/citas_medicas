from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List
from .base_schema import BaseSchema

class ConsultaBase(BaseModel):
    cedula: str
    fecha: datetime
    diagnostico: str
    prescripcion: str
    ordenes: str

class ConsultaCreate(ConsultaBase):
    pass

class ConsultaOut(ConsultaBase):  # <-- Esta es la clase que faltaba
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

class Consulta(ConsultaBase):
    id: int

    class Config:
        from_attributes = True
