from fastapi import FastAPI
from controllers import paciente_controller, usuario_controller, citas_controller, consultas_controller, certificados_controller

from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(paciente_controller.router, prefix="/api")
app.include_router(usuario_controller.router, prefix="/api")
app.include_router(citas_controller.router, prefix="/api")
app.include_router(consultas_controller.router, prefix="/api")
app.include_router(certificados_controller.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Sistema de Citas Médicas"}