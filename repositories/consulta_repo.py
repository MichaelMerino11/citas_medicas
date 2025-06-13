from sqlalchemy.orm import Session
from models.consulta import Consulta
from schemas.consulta_schema import ConsultaCreate

def crear_consulta(db: Session, consulta: ConsultaCreate):
    db_consulta = Consulta(**consulta.dict())
    db.add(db_consulta)
    db.commit()
    db.refresh(db_consulta)
    return db_consulta
