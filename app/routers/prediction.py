from fastapi import APIRouter

from app.schemas.request import PredictionRequest
from app.schemas.response import PredictionResponse
from app.services.prediction_service import PredictionService
from src.pipeline.prediction_pipeline import CustomData

router = APIRouter(
    prefix="/predict",
    tags=["Prediction"],
)

service = PredictionService()


@router.post("/", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    data = CustomData(**request.model_dump())

    prediction = service.predict(data)

    return PredictionResponse(predicted_price=prediction)
