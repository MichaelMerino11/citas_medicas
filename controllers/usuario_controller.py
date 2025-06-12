from fastapi import APIRouter, Depends
from schemas.usuario_schema import UsuarioCreate, Usuario
from services.usuario_service import UsuarioService
from database import get_db

router = APIRouter()

@router.post("/usuarios/", response_model=Usuario)
def crear_usuario(usuario: UsuarioCreate, db = Depends(get_db)):
    service = UsuarioService(db)
    return service.crear_usuario(usuario)

@router.get("/usuarios/{usuario_id}", response_model=Usuario)
def obtener_usuario(usuario_id: int, db = Depends(get_db)):
    service = UsuarioService(db)
    return service.obtener_usuario(usuario_id)