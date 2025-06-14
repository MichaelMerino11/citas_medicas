from fastapi import APIRouter, Depends
from typing import List
from database import get_db
from schemas.finanzas_schema import TransaccionCreate, TransaccionOut, ComprobanteCreate, ComprobanteOut
from services.finanzas_service import FinanzasService

router = APIRouter(prefix="/api/finanzas", tags=["finanzas"])

@router.post("/transacciones/", response_model=TransaccionOut)
def create_transaccion(transaccion: TransaccionCreate, db=Depends(get_db)):
    return FinanzasService(db).crear_transaccion(transaccion)

@router.post("/comprobantes/", response_model=ComprobanteOut)
def create_comprobante(comprobante: ComprobanteCreate, db=Depends(get_db)):
    return FinanzasService(db).crear_comprobante(comprobante)

@router.get("/comprobantes/{comprobante_id}/transacciones", response_model=List[TransaccionOut])
def get_transacciones_comprobante(comprobante_id: str, db=Depends(get_db)):
    return FinanzasService(db).get_transacciones_comprobante(comprobante_id)

@router.get("/pacientes/{paciente_id}/comprobantes", response_model=List[ComprobanteOut])
def get_comprobantes_paciente(paciente_id: str, db=Depends(get_db)):
    return FinanzasService(db).get_comprobantes_paciente(paciente_id)