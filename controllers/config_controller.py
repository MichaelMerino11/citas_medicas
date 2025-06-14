from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from database import get_db
from schemas.config_schema import (
    ConfiguracionBase,
    ConfiguracionUpdate,
    UsuarioCreate,
    UsuarioOut,
    UsuarioUpdate
)
from services.config_service import ConfiguracionService, UsuarioService

router = APIRouter(
    prefix="/api/config",
    tags=["configuracion"]
)

# Endpoints de Configuración General
@router.get("/", response_model=ConfiguracionBase)
def get_config(db=Depends(get_db)):
    return ConfiguracionService(db).get_config()

@router.patch("/", response_model=ConfiguracionBase)
def update_config(config_data: ConfiguracionUpdate, db=Depends(get_db)):
    return ConfiguracionService(db).update_config(config_data)

# Endpoints de Usuarios
@router.post("/usuarios/", response_model=UsuarioOut, status_code=status.HTTP_201_CREATED)
def create_usuario(usuario: UsuarioCreate, db=Depends(get_db)):
    return UsuarioService(db).create_usuario(usuario)

@router.get("/usuarios/{username}", response_model=UsuarioOut)
def get_usuario(username: str, db=Depends(get_db)):
    return UsuarioService(db).get_usuario(username)

@router.patch("/usuarios/{username}", response_model=UsuarioOut)
def update_usuario(username: str, usuario_data: UsuarioUpdate, db=Depends(get_db)):
    return UsuarioService(db).update_usuario(username, usuario_data)