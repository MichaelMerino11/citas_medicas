from sqlalchemy.orm import Session
from models.certificado import Certificado
from schemas.certificado_schema import CertificadoCreate

def crear_certificado(db: Session, certificado: CertificadoCreate):
    db_cert = Certificado(**certificado.dict())
    db.add(db_cert)
    db.commit()
    db.refresh(db_cert)
    return db_cert
