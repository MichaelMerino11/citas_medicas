from pydantic import BaseModel, EmailStr
from typing import Optional, Dict, Any
from datetime import datetime
from enum import Enum

class Perfil(str, Enum):
    admin = "admin"
    medico = "medico"
    recepcion = "recepcion"

class UsuarioBase(BaseModel):
    username: str
    email: EmailStr
    perfil: Perfil

class UsuarioCreate(UsuarioBase):
    password: str

class UsuarioUpdate(BaseModel):
    email: Optional[EmailStr] = None
    perfil: Optional[Perfil] = None
    password: Optional[str] = None
    activo: Optional[bool] = None

class UsuarioOut(UsuarioBase):
    id: str
    activo: bool
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class ConfiguracionBase(BaseModel):
    parametros_generales: Dict[str, Any]
    plan_cuentas: Dict[str, Any]

class ConfiguracionUpdate(BaseModel):
    parametros_generales: Optional[Dict[str, Any]] = None
    plan_cuentas: Optional[Dict[str, Any]] = None