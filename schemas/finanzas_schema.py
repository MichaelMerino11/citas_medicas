from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List
from schemas.base_schema import BaseSchema

class TransaccionBase(BaseSchema):
    tipo: str  # ingreso/egreso
    monto: float
    descripcion: str
    comprobante_id: Optional[str] = None
    cuenta_contable: str
    paciente_id: Optional[str] = None
    medico_id: Optional[str] = None

class TransaccionCreate(TransaccionBase):
    pass

class TransaccionOut(TransaccionBase):
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

class ComprobanteBase(BaseSchema):
    numero: str
    monto_total: float
    paciente_id: str
    transacciones: List[str]

class ComprobanteCreate(ComprobanteBase):
    pass

class ComprobanteOut(ComprobanteBase):
    id: str
    fecha: datetime
    created_at: datetime
    updated_at: Optional[datetime] = None