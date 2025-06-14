from fastapi import FastAPI
from database import Base, engine
from controllers import (
    #config_controller,      # 8.2.1 Configuración
    paciente_controller,   # 8.2.2 Pacientes
    colaboradores_controller, # 8.2.3 Colaboradores
    citas_controller,       # 8.2.4 Citas
    consultas_controller,   # 8.2.5 Consultas
    certificados_controller, # 8.2.6 Certificados
    finanzas_controller,    # 8.2.7 Finanzas
    reportes_controller     # 8.2.8 Reportes
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sistema de Citas Médicas",
    description="API para gestión de consultorio médico",
    version="1.0.0"
)

#app.include_router(config_controller.router, prefix="/api")
app.include_router(paciente_controller.router, prefix="/api")
app.include_router(colaboradores_controller.router, prefix="/api")
app.include_router(citas_controller.router, prefix="/api")
app.include_router(consultas_controller.router, prefix="/api")
app.include_router(certificados_controller.router, prefix="/api")
app.include_router(finanzas_controller.router, prefix="/api")
app.include_router(reportes_controller.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "API de Citas Médicas"}