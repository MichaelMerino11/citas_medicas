from fastapi import APIRouter, Depends
from typing import List, Dict
from datetime import date
from database import get_db
from services.reportes_service import ReportesService

router = APIRouter(prefix="/api/reportes", tags=["reportes"])

@router.get("/libro-diario/{fecha}", response_model=List[Dict])
def libro_diario(fecha: date, db=Depends(get_db)):
    return ReportesService(db).libro_diario(fecha)

@router.get("/historia-clinica/{paciente_id}", response_model=List[Dict])
def historia_clinica(paciente_id: str, db=Depends(get_db)):
    return ReportesService(db).historia_clinica(paciente_id)

@router.get("/resumen-comprobantes/", response_model=Dict)
def resumen_comprobantes(
    fecha_inicio: date, 
    fecha_fin: date, 
    db=Depends(get_db)
):
    return ReportesService(db).resumen_comprobantes(fecha_inicio, fecha_fin)