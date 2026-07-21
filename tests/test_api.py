from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Laptop Price Prediction API is running!"}


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_predict():
    payload = {
        "Company": "Dell",
        "Product": "Inspiron 15",
        "TypeName": "Notebook",
        "Inches": 15.6,
        "Ram": 8,
        "OS": "Windows 10",
        "Weight": 2.1,
        "Screen": "Full HD",
        "ScreenW": 1920,
        "ScreenH": 1080,
        "Touchscreen": 0,
        "IPSpanel": 1,
        "RetinaDisplay": 0,
        "CPU_company": "Intel",
        "CPU_freq": 2.5,
        "CPU_model": "Core i5",
        "PrimaryStorage": 256,
        "SecondaryStorage": 0,
        "PrimaryStorageType": "SSD",
        "SecondaryStorageType": "None",
        "GPU_company": "Intel",
        "GPU_model": "HD Graphics 620",
    }

    response = client.post("/predict/", json=payload)

    assert response.status_code == 200

    body = response.json()

    assert "predicted_price" in body
    assert isinstance(body["predicted_price"], float)
