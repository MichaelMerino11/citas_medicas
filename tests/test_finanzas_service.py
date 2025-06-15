import pytest
import uuid
from services.finanzas_service import FinanzasService
from schemas.finanzas_schema import ComprobanteCreate
from models.finanzas import Comprobante
from unittest.mock import MagicMock
from sqlalchemy.orm import Session

@pytest.fixture
def fake_db():
    return MagicMock(spec=Session)

def test_crear_comprobante(fake_db):
    # Arrange
    comprobante_data = ComprobanteCreate(
        numero="FAC-2025-001234",
        monto_total=250.00,
        paciente_id="987654321",
        transacciones=[
            "Pago por consulta médica: 150.00",
            "Exámenes de laboratorio: 100.00"
        ]
    )
    
    # Simular la conversión a Comprobante (lo que hace FinanzasService)
    comprobante_dict = comprobante_data.dict()
    comprobante_dict["id"] = str(uuid.uuid4())  # Genera un ID único
    comprobante_orm = Comprobante(**comprobante_dict)
    
    # Crear el servicio con el mock de la base de datos
    service = FinanzasService(fake_db)
    
    # Mock repository method
    service.comprobante_repo.create = MagicMock(return_value="ComprobanteCreado")
    
    # Act
    resultado = service.crear_comprobante(comprobante_data)
    
    # Assert
    assert resultado == "ComprobanteCreado"
    
    # Verificar que se llamó con el objeto Comprobante convertido
    service.comprobante_repo.create.assert_called_once_with(comprobante_orm)