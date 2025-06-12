from pydantic import BaseModel
from typing import Optional

class PacienteBase(BaseModel):
    cedula: str
    nombre: str
    email: str

class PacienteCreate(PacienteBase):
    direccion: Optional[str] = None
    telefono: Optional[str] = None
    facturacion_terceros: bool = False
    datos_facturacion: Optional[str] = None

class Paciente(PacienteBase):
    id: int
    activo: bool

    class Config:
        from_attributes = True  # Cambia orm_mode a from_attributes (Pydantic V2)