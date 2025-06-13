from fastapi import APIRouter, Depends
from schemas.consulta_schema import ConsultaCreate, Consulta
from services.consulta_service import ConsultaService
from database import get_db

router = APIRouter()

@router.post("/consultas/", response_model=Consulta)
def registrar_consulta(consulta: ConsultaCreate, db=Depends(get_db)):
    return ConsultaService(db).crear_consulta(consulta)
