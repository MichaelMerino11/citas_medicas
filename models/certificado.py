from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class Certificado(Base):
    __tablename__ = "certificados"

    id = Column(Integer, primary_key=True, index=True)
    cedula = Column(String)
    fecha_emision = Column(DateTime)
    contenido = Column(String)
