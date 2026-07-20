from src.pipeline.prediction_pipeline import (
    CustomData,
    PredictPipeline,
)


class PredictionService:
    """Service layer for laptop price prediction."""

    def __init__(self):
        self.pipeline = PredictPipeline()

    def predict(self, data: CustomData):
        df = data.get_data_as_dataframe()

        prediction = self.pipeline.predict(df)

        return float(prediction[0])