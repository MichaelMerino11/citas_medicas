from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from schemas.base_schema import BaseSchema

class MedicoBase(BaseSchema):
    cedula: str
    nombre: str
    especialidad: str
    telefono: Optional[str] = None
    email: Optional[str] = None

class MedicoCreate(MedicoBase):
    pass

class MedicoOut(MedicoBase):
    id: str
    activo: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

class ColaboradorBase(BaseSchema):
    cedula: str
    nombre: str
    rol: str
    telefono: Optional[str] = None
    email: Optional[str] = None

class ColaboradorCreate(ColaboradorBase):
    pass

class ColaboradorOut(ColaboradorBase):
    id: str
    activo: bool
    created_at: datetime
    updated_at: Optional[datetime] = None