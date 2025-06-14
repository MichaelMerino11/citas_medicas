from typing import Optional
from sqlalchemy.orm import Session
from models.config import Configuracion, Usuario
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class ConfiguracionRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_config(self) -> Configuracion:
        return self.db.query(Configuracion).first()
    
    def update_config(self, config_data: dict) -> Configuracion:
        config = self.get_config()
        if not config:
            config = Configuracion()
            self.db.add(config)
        
        for key, value in config_data.items():
            setattr(config, key, value)
        
        self.db.commit()
        self.db.refresh(config)
        return config

class UsuarioRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_by_username(self, username: str) -> Optional[Usuario]:
        return self.db.query(Usuario).filter(Usuario.username == username).first()
    
    def get_by_email(self, email: str) -> Optional[Usuario]:
        return self.db.query(Usuario).filter(Usuario.email == email).first()
    
    def create(self, usuario: UsuarioCreate) -> Usuario:
        hashed_password = pwd_context.hash(usuario.password)
        db_usuario = Usuario(
            username=usuario.username,
            email=usuario.email,
            hashed_password=hashed_password,
            perfil=usuario.perfil
        )
        self.db.add(db_usuario)
        self.db.commit()
        self.db.refresh(db_usuario)
        return db_usuario
    
    def update(self, username: str, usuario_data: UsuarioUpdate) -> Optional[Usuario]:
        usuario = self.get_by_username(username)
        if not usuario:
            return None
        
        if usuario_data.password:
            usuario.hashed_password = pwd_context.hash(usuario_data.password)
        if usuario_data.email:
            usuario.email = usuario_data.email
        if usuario_data.perfil:
            usuario.perfil = usuario_data.perfil
        if usuario_data.activo is not None:
            usuario.activo = usuario_data.activo
        
        self.db.commit()
        self.db.refresh(usuario)
        return usuario