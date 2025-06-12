from repositories.paciente_repository import crear_paciente, obtener_paciente_por_cedula
from schemas.paciente_schema import PacienteCreate

class PacienteService:
    def __init__(self, db):
        self.db = db

    def crear_paciente(self, paciente: PacienteCreate):
        return crear_paciente(self.db, paciente)

    def buscar_por_cedula(self, cedula: str):
        return obtener_paciente_por_cedula(self.db, cedula)