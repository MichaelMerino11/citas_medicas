from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_post_comprobante():
    payload = {
        "numero": "FAC-2025-001234",
        "monto_total": 250.00,
        "paciente_id": "987654321",
        "transacciones": [
            "Pago por consulta médica: 150.00",
            "Exámenes de laboratorio: 100.00"
        ]
    }

    response = client.post("/api/api/finanzas/comprobantes/", json=payload)

    # Puedes adaptar según el comportamiento esperado
    assert response.status_code in [200, 201]
    assert "numero" in response.json()
