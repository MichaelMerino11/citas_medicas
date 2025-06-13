from sqlalchemy import Column, Integer, String, DateTime, Enum
from database import Base
import enum

class EstadoCita(str, enum.Enum):
    pendiente = "pendiente"
    cancelada = "cancelada"
    atendida = "atendida"

class Cita(Base):
    __tablename__ = "citas"

    id = Column(Integer, primary_key=True, index=True)
    cedula = Column(String)
    fecha = Column(DateTime)
    motivo = Column(String)
    estado = Column(Enum(EstadoCita), default="pendiente")
