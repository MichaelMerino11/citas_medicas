from sqlalchemy.orm import Session
from models.paciente import Paciente
from schemas.paciente_schema import PacienteCreate  # Importar el esquema

def crear_paciente(db: Session, paciente: PacienteCreate):
    db_paciente = Paciente(**paciente.dict())
    db.add(db_paciente)
    db.commit()
    db.refresh(db_paciente)
    return db_paciente

def obtener_paciente_por_cedula(db: Session, cedula: str):
    return db.query(Paciente).filter(Paciente.cedula == cedula).first()