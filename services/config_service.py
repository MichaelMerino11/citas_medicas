from typing import Optional
from sqlalchemy.orm import Session
from models.config import Configuracion, Usuario
from schemas.config_schema import (
    ConfiguracionBase,
    ConfiguracionUpdate,
    UsuarioCreate,
    UsuarioOut,
    UsuarioUpdate
)
from repositories.config_repository import ConfiguracionRepository, UsuarioRepository
from fastapi import HTTPException, status

class ConfiguracionService:
    def __init__(self, db: Session):
        self.repository = ConfiguracionRepository(db)
    
    def get_config(self) -> ConfiguracionBase:
        config = self.repository.get_config()
        if not config:
            config = Configuracion()
            self.repository.db.add(config)
            self.repository.db.commit()
            self.repository.db.refresh(config)
        return config
    
    def update_config(self, config_data: ConfiguracionUpdate) -> ConfiguracionBase:
        return self.repository.update_config(config_data.dict(exclude_unset=True))

class UsuarioService:
    def __init__(self, db: Session):
        self.repository = UsuarioRepository(db)
    
    def create_usuario(self, usuario: UsuarioCreate) -> UsuarioOut:
        if self.repository.get_by_username(usuario.username):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El nombre de usuario ya existe"
            )
        
        if self.repository.get_by_email(usuario.email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El email ya está registrado"
            )
        
        return self.repository.create(usuario)
    
    def update_usuario(self, username: str, usuario_data: UsuarioUpdate) -> UsuarioOut:
        usuario = self.repository.update(username, usuario_data)
        if not usuario:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Usuario no encontrado"
            )
        return usuario
    
    def get_usuario(self, username: str) -> UsuarioOut:
        usuario = self.repository.get_by_username(username)
        if not usuario:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Usuario no encontrado"
            )
        return usuario