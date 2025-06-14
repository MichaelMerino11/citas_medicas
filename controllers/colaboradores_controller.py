from fastapi import APIRouter, Depends
from typing import List
from database import get_db
from schemas.colaboradores_schema import MedicoCreate, MedicoOut, ColaboradorCreate, ColaboradorOut
from services.colaboradores_service import MedicoService, ColaboradorService

router = APIRouter(prefix="/api/colaboradores", tags=["colaboradores"])

@router.post("/medicos/", response_model=MedicoOut)
def create_medico(medico: MedicoCreate, db=Depends(get_db)):
    return MedicoService(db).create(medico)

@router.get("/medicos/{cedula}", response_model=MedicoOut)
def get_medico(cedula: str, db=Depends(get_db)):
    return MedicoService(db).get_by_cedula(cedula)

@router.post("/colaboradores/", response_model=ColaboradorOut)
def create_colaborador(colaborador: ColaboradorCreate, db=Depends(get_db)):
    return ColaboradorService(db).create(colaborador)

@router.get("/colaboradores/{cedula}", response_model=ColaboradorOut)
def get_colaborador(cedula: str, db=Depends(get_db)):
    return ColaboradorService(db).get_by_cedula(cedula)