from app.services.prediction_service import PredictionService
from src.pipeline.prediction_pipeline import CustomData


def test_prediction_service():
    service = PredictionService()

    data = CustomData(
        Company="Dell",
        Product="Inspiron 15",
        TypeName="Notebook",
        Inches=15.6,
        Ram=8,
        OS="Windows 10",
        Weight=2.1,
        Screen="Full HD",
        ScreenW=1920,
        ScreenH=1080,
        Touchscreen=0,
        IPSpanel=1,
        RetinaDisplay=0,
        CPU_company="Intel",
        CPU_freq=2.5,
        CPU_model="Core i5",
        PrimaryStorage=256,
        SecondaryStorage=0,
        PrimaryStorageType="SSD",
        SecondaryStorageType="None",
        GPU_company="Intel",
        GPU_model="HD Graphics 620",
    )

    prediction = service.predict(data)

    assert isinstance(prediction, float)
