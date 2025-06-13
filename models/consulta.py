from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from database import Base

class Consulta(Base):
    __tablename__ = "consultas"

    id = Column(Integer, primary_key=True, index=True)
    cedula = Column(String)
    fecha = Column(DateTime)
    diagnostico = Column(String)
    prescripcion = Column(String)
    ordenes = Column(String)
