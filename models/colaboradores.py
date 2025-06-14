from sqlalchemy import Column, String, Boolean
from sqlalchemy.sql import func
from models.base import BaseModel
import uuid

class Medico(BaseModel):
    __tablename__ = "medicos"
    
    # Asegúrate que el ID tenga autoincremento o un valor por defecto
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))  # Genera UUID automático
    cedula = Column(String, unique=True, index=True)
    nombre = Column(String)
    especialidad = Column(String)
    telefono = Column(String, nullable=True)
    email = Column(String, nullable=True)
    activo = Column(Boolean, default=True)

class Colaborador(BaseModel):
    __tablename__ = "colaboradores"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))  # Genera UUID automático
    cedula = Column(String, unique=True, index=True)
    nombre = Column(String)
    rol = Column(String)
    telefono = Column(String, nullable=True)
    email = Column(String, nullable=True)
    activo = Column(Boolean, default=True)