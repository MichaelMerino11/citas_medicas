from typing import List
from sqlalchemy.orm import Session
from models.colaboradores import Medico, Colaborador
from schemas.colaboradores_schema import (
    MedicoCreate,  # <-- Añade esta importación
    MedicoOut,
    ColaboradorCreate,  # <-- Añade esta importación
    ColaboradorOut
)
from repositories.colaboradores_repository import MedicoRepository, ColaboradorRepository

class MedicoService:
    def __init__(self, db: Session):
        self.repository = MedicoRepository(db)
    
    def create(self, medico_data: MedicoCreate) -> MedicoOut:
        db_medico = self.repository.create(medico_data)
        # Convertir el modelo SQLAlchemy a esquema Pydantic para la respuesta
        return MedicoOut.from_orm(db_medico)
    
    def get_by_cedula(self, cedula: str) -> MedicoOut:
        db_medico = self.repository.get_by_cedula(cedula)
        if db_medico:
            return MedicoOut.from_orm(db_medico)
        return None

from sqlalchemy.orm import Session
from schemas.colaboradores_schema import MedicoOut, ColaboradorOut
from repositories.colaboradores_repository import MedicoRepository, ColaboradorRepository
from models.colaboradores import Medico, Colaborador

class MedicoService:
    def __init__(self, db: Session):
        self.repository = MedicoRepository(db)
    
    def create(self, medico_data: MedicoCreate) -> MedicoOut:
        db_medico = self.repository.create(medico_data)
        # Convertir el modelo SQLAlchemy a esquema Pydantic para la respuesta
        return MedicoOut.from_orm(db_medico)
    
    def get_by_cedula(self, cedula: str) -> MedicoOut:
        db_medico = self.repository.get_by_cedula(cedula)
        if db_medico:
            return MedicoOut.from_orm(db_medico)
        return None

class ColaboradorService:
    def __init__(self, db: Session):
        self.repository = ColaboradorRepository(db)
    
    def create(self, colaborador_data: ColaboradorCreate) -> ColaboradorOut:
        db_colaborador = self.repository.create(colaborador_data)
        return ColaboradorOut.from_orm(db_colaborador)
    
    def get_by_cedula(self, cedula: str) -> ColaboradorOut:
        db_colaborador = self.repository.get_by_cedula(cedula)
        if db_colaborador:
            return ColaboradorOut.from_orm(db_colaborador)
        return None