from sqlalchemy import Column, String, Float, DateTime, ForeignKey, JSON
from sqlalchemy.sql import func
from models.base import BaseModel

class Transaccion(BaseModel):
    __tablename__ = "transacciones"
    
    tipo = Column(String)  # ingreso/egreso
    monto = Column(Float)
    descripcion = Column(String)
    comprobante_id = Column(String)
    cuenta_contable = Column(String)
    paciente_id = Column(String, ForeignKey("pacientes.id"), nullable=True)
    medico_id = Column(String, ForeignKey("medicos.id"), nullable=True)

class Comprobante(BaseModel):
    __tablename__ = "comprobantes"
    
    numero = Column(String, unique=True)
    fecha = Column(DateTime, server_default=func.now())
    monto_total = Column(Float)
    paciente_id = Column(String, ForeignKey("pacientes.id"))
    transacciones = Column(JSON)  # Lista de IDs de transacciones