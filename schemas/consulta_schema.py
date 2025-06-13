from pydantic import BaseModel
from datetime import datetime

class ConsultaBase(BaseModel):
    cedula: str
    fecha: datetime
    diagnostico: str
    prescripcion: str
    ordenes: str

class ConsultaCreate(ConsultaBase):
    pass

class Consulta(ConsultaBase):
    id: int

    class Config:
        from_attributes = True
