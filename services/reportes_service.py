from typing import List, Dict
from sqlalchemy.orm import Session
from datetime import date, timedelta
from models.finanzas import Transaccion, Comprobante
from models.consulta import Consulta
from models.paciente import Paciente
from schemas.finanzas_schema import TransaccionOut, ComprobanteOut
from schemas.consulta_schema import ConsultaOut

class ReportesService:
    def __init__(self, db: Session):
        self.db = db
    
    def libro_diario(self, fecha: date) -> List[Dict]:
        transacciones = self.db.query(Transaccion)\
            .filter(func.date(Transaccion.created_at) == fecha)\
            .all()
        
        return [
            {
                "fecha": t.created_at,
                "cuenta": t.cuenta_contable,
                "descripcion": t.descripcion,
                "debito": t.monto if t.tipo == "egreso" else 0,
                "credito": t.monto if t.tipo == "ingreso" else 0
            }
            for t in transacciones
        ]
    
    def historia_clinica(self, paciente_id: str) -> List[ConsultaOut]:
        return self.db.query(Consulta)\
            .filter(Consulta.paciente_id == paciente_id)\
            .order_by(Consulta.created_at.desc())\
            .all()
    
    def resumen_comprobantes(self, fecha_inicio: date, fecha_fin: date) -> Dict:
        comprobantes = self.db.query(Comprobante)\
            .filter(Comprobante.fecha >= fecha_inicio, Comprobante.fecha <= fecha_fin)\
            .all()
        
        total = sum(c.monto_total for c in comprobantes)
        
        return {
            "periodo": f"{fecha_inicio} a {fecha_fin}",
            "cantidad": len(comprobantes),
            "total": total,
            "comprobantes": comprobantes
        }