from sqlalchemy.orm import Session
from models.usuario import Usuario
from schemas.usuario_schema import UsuarioCreate  # Importa el esquema
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def crear_usuario(db: Session, usuario: UsuarioCreate):
    hashed_password = pwd_context.hash(usuario.password)
    db_usuario = Usuario(
        email=usuario.email,
        hashed_password=hashed_password,
        perfil=usuario.perfil
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def obtener_usuario(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()