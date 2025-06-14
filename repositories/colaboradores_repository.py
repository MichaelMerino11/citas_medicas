from sqlalchemy.orm import Session
from models.colaboradores import Medico, Colaborador
from schemas.colaboradores_schema import MedicoCreate, ColaboradorCreate

class MedicoRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, medico_data: MedicoCreate) -> Medico:
        db_medico = Medico(
            cedula=medico_data.cedula,
            nombre=medico_data.nombre,
            especialidad=medico_data.especialidad,
            telefono=medico_data.telefono,
            email=medico_data.email
        )
        self.db.add(db_medico)
        self.db.commit()
        self.db.refresh(db_medico)
        return db_medico
    
    def get_by_cedula(self, cedula: str) -> Medico:
        return self.db.query(Medico).filter(Medico.cedula == cedula).first()

class ColaboradorRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, colaborador_data: ColaboradorCreate) -> Colaborador:  # <-- Cambiado a ColaboradorCreate
        db_colaborador = Colaborador(
            cedula=colaborador_data.cedula,
            nombre=colaborador_data.nombre,
            rol=colaborador_data.rol,  # <-- Usar rol en lugar de especialidad
            telefono=colaborador_data.telefono,
            email=colaborador_data.email
        )
        self.db.add(db_colaborador)
        self.db.commit()
        self.db.refresh(db_colaborador)
        return db_colaborador
    
    def get_by_cedula(self, cedula: str) -> Colaborador:
        return self.db.query(Colaborador).filter(Colaborador.cedula == cedula).first()