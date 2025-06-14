from typing import List
from sqlalchemy.orm import Session
from models.finanzas import Transaccion, Comprobante
from repositories.base_repository import BaseRepository

class TransaccionRepository(BaseRepository[Transaccion]):
    def __init__(self, db: Session):
        super().__init__(Transaccion, db)
    
    def get_by_comprobante(self, comprobante_id: str) -> List[Transaccion]:
        return self.db.query(self.model).filter(self.model.comprobante_id == comprobante_id).all()
    
    def get_by_cuenta(self, cuenta: str) -> List[Transaccion]:
        return self.db.query(self.model).filter(self.model.cuenta_contable == cuenta).all()

class ComprobanteRepository(BaseRepository[Comprobante]):
    def __init__(self, db: Session):
        super().__init__(Comprobante, db)
    
    def get_by_numero(self, numero: str) -> Comprobante:
        return self.db.query(self.model).filter(self.model.numero == numero).first()
    
    def get_by_paciente(self, paciente_id: str) -> List[Comprobante]:
        return self.db.query(self.model).filter(self.model.paciente_id == paciente_id).all()