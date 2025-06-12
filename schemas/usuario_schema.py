from pydantic import BaseModel

class UsuarioBase(BaseModel):
    email: str
    perfil: str  # "admin", "medico", "recepcionista"

class UsuarioCreate(UsuarioBase):
    password: str

class Usuario(UsuarioBase):
    id: int
    activo: bool

    class Config:
        from_attributes = True