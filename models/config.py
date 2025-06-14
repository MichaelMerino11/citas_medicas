from sqlalchemy import Column, String, Boolean, JSON
from models.base import BaseModel

class Configuracion(BaseModel):
    __tablename__ = "configuraciones"
    
    parametros_generales = Column(JSON, default={
        "hora_inicio_atencion": "08:00",
        "hora_fin_atencion": "17:00",
        "duracion_cita": 30,
        "dias_atencion": ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    })
    
    plan_cuentas = Column(JSON, default={
        "ingresos": {
            "consultas": "4.1.1.01",
            "procedimientos": "4.1.1.02"
        },
        "egresos": {
            "gastos_administrativos": "5.1.1.01",
            "gastos_medicos": "5.1.1.02"
        }
    })

class Usuario(BaseModel):
    __tablename__ = "usuarios"
    
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(255))
    perfil = Column(String(20))  # admin, medico, recepcion
    activo = Column(Boolean, default=True)
    
    # Relación con configuración específica del usuario
    configuracion = Column(JSON, default={
        "theme": "light",
        "language": "es"
    })