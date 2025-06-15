from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from models.base import BaseModel

class Consulta(BaseModel):
    __tablename__ = "consultas"

    paciente_id = Column(String, ForeignKey("pacientes.id"))  # Cambiado de cedula a paciente_id
    medico_id = Column(String, ForeignKey("medicos.id"))
    fecha = Column(DateTime, server_default=func.now())
    diagnostico = Column(String)
    prescripcion = Column(String)
    ordenes = Column(String)