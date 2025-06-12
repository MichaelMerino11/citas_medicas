from repositories.usuario_repository import crear_usuario, obtener_usuario
from schemas.usuario_schema import UsuarioCreate

class UsuarioService:
    def __init__(self, db):
        self.db = db

    def crear_usuario(self, usuario: UsuarioCreate):
        return crear_usuario(self.db, usuario)

    def obtener_usuario(self, usuario_id: int):
        return obtener_usuario(self.db, usuario_id)