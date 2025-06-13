from pydantic import BaseModel
from datetime import datetime
from typing import Literal

class CitaBase(BaseModel):
    cedula: str
    fecha: datetime
    motivo: str

class CitaCreate(CitaBase):
    pass

class Cita(CitaBase):
    id: int
    estado: Literal["pendiente", "cancelada", "atendida"]

    class Config:
        from_attributes = True
