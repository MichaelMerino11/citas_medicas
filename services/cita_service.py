from sqlalchemy.orm import Session
from repositories import cita_repo
from schemas.cita_schema import CitaCreate

class CitaService:
    def __init__(self, db: Session):
        self.db = db

    def crear_cita(self, cita: CitaCreate):
        return cita_repo.crear_cita(self.db, cita)

    def listar_por_cedula(self, cedula: str):
        return cita_repo.obtener_citas_por_cedula(self.db, cedula)
