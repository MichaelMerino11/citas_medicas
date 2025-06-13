from sqlalchemy.orm import Session
from repositories import consulta_repo
from schemas.consulta_schema import ConsultaCreate

class ConsultaService:
    def __init__(self, db: Session):
        self.db = db

    def crear_consulta(self, consulta: ConsultaCreate):
        return consulta_repo.crear_consulta(self.db, consulta)
