from fastapi import APIRouter, Depends
from schemas.certificado_schema import CertificadoCreate, Certificado
from services.certificado_service import CertificadoService
from database import get_db

router = APIRouter()

@router.post("/certificados/", response_model=Certificado)
def emitir_certificado(certificado: CertificadoCreate, db=Depends(get_db)):
    return CertificadoService(db).emitir_certificado(certificado)
