from typing import List
from sqlalchemy.orm import Session
from models.finanzas import Transaccion, Comprobante
from schemas.finanzas_schema import (
    TransaccionCreate,  # <-- Añade esta importación
    TransaccionOut,
    ComprobanteCreate,  # <-- Añade esta importación
    ComprobanteOut
)
import uuid 
from repositories.finanzas_repository import TransaccionRepository, ComprobanteRepository

class FinanzasService:
    def __init__(self, db: Session):
        self.transaccion_repo = TransaccionRepository(db)
        self.comprobante_repo = ComprobanteRepository(db)
    
    def crear_transaccion(self, transaccion: TransaccionCreate) -> TransaccionOut:
        transaccion_dict = transaccion.dict()
        transaccion_dict["id"] = str(uuid.uuid4())  # Genera un ID único
        transaccion_orm = Transaccion(**transaccion_dict)
        return self.transaccion_repo.create(transaccion_orm)

    
    def crear_comprobante(self, comprobante: ComprobanteCreate) -> ComprobanteOut:
        comprobante_dict = comprobante.dict()
        comprobante_dict["id"] = str(uuid.uuid4())  # si tu modelo hereda de BaseModel con id
        comprobante_orm = Comprobante(**comprobante_dict)
        return self.comprobante_repo.create(comprobante_orm)

    
    def get_transacciones_comprobante(self, comprobante_id: str) -> List[TransaccionOut]:
        return self.transaccion_repo.get_by_comprobante(comprobante_id)
    
    def get_comprobantes_paciente(self, paciente_id: str) -> List[ComprobanteOut]:
        return self.comprobante_repo.get_by_paciente(paciente_id)