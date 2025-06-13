from pydantic import BaseModel
from datetime import datetime

class CertificadoBase(BaseModel):
    cedula: str
    fecha_emision: datetime
    contenido: str

class CertificadoCreate(CertificadoBase):
    pass

class Certificado(CertificadoBase):
    id: int

    class Config:
        from_attributes = True
