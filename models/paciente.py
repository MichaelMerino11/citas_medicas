from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from database import Base

class Paciente(Base):
    __tablename__ = "pacientes"

    id = Column(Integer, primary_key=True, index=True)
    cedula = Column(String, unique=True, index=True)
    nombre = Column(String)
    email = Column(String)
    direccion = Column(String, nullable=True)
    telefono = Column(String, nullable=True)
    facturacion_terceros = Column(Boolean, default=False)
    datos_facturacion = Column(String, nullable=True)
    activo = Column(Boolean, default=True)  # Nuevo campo