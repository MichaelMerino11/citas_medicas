from fastapi import APIRouter, Depends
from schemas.cita_schema import CitaCreate, Cita
from services.cita_service import CitaService
from database import get_db
from typing import List

router = APIRouter(prefix="/api/citas", tags=["citas"])

@router.post("/citas/", response_model=Cita)
def crear_cita(cita: CitaCreate, db=Depends(get_db)):
    return CitaService(db).crear_cita(cita)

@router.get("/citas/{cedula}", response_model=List[Cita])
def listar_citas(cedula: str, db=Depends(get_db)):
    return CitaService(db).listar_por_cedula(cedula)
