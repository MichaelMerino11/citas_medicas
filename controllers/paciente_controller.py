from fastapi import APIRouter, Depends
from schemas.paciente_schema import PacienteCreate, Paciente
from services.paciente_service import PacienteService
from database import get_db  # Ahora esta importación funcionará

router = APIRouter()

@router.post("/pacientes/", response_model=Paciente)
def crear_paciente(paciente: PacienteCreate, db = Depends(get_db)):
    service = PacienteService(db)
    return service.crear_paciente(paciente)

@router.get("/pacientes/{cedula}", response_model=Paciente)
def buscar_paciente(cedula: str, db = Depends(get_db)):
    service = PacienteService(db)
    return service.buscar_por_cedula(cedula)