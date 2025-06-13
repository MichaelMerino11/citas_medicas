from sqlalchemy.orm import Session
from models.cita import Cita
from schemas.cita_schema import CitaCreate

def crear_cita(db: Session, cita: CitaCreate):
    db_cita = Cita(**cita.dict())
    db.add(db_cita)
    db.commit()
    db.refresh(db_cita)
    return db_cita

def obtener_citas_por_cedula(db: Session, cedula: str):
    return db.query(Cita).filter(Cita.cedula == cedula).all()
