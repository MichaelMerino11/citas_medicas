from sqlalchemy.orm import Session
from repositories import certificado_repo
from schemas.certificado_schema import CertificadoCreate

class CertificadoService:
    def __init__(self, db: Session):
        self.db = db

    def emitir_certificado(self, certificado: CertificadoCreate):
        return certificado_repo.crear_certificado(self.db, certificado)
