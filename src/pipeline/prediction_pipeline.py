import sys
from dataclasses import dataclass

import pandas as pd

from src.config import (
    DataTransformationConfig,
    ModelTrainerConfig,
)
from src.exception import CustomException
from src.logger import logger
from src.utils import load_pickle


class PredictPipeline:
    def __init__(self):
        try:
            logger.info("Loading trained model...")

            self.model = load_pickle(ModelTrainerConfig().trained_model_path)

            logger.info("Loading preprocessor...")

            self.preprocessor = load_pickle(
                DataTransformationConfig().preprocessor_path
            )

            logger.info("Prediction pipeline initialized successfully.")

        except Exception as e:
            logger.exception("Failed to initialize prediction pipeline.")
            raise CustomException(e, sys) from e

    def predict(
        self,
        features: pd.DataFrame,
    ):
        try:
            logger.info("Starting prediction...")

            transformed_features = self.preprocessor.transform(features)

            predictions = self.model.predict(transformed_features)

            return predictions

        except Exception as e:
            logger.exception("Prediction failed.")
            raise CustomException(e, sys) from e


@dataclass
class CustomData:
    """
    Represents a single laptop for prediction.
    """

    Company: str
    Product: str
    TypeName: str
    Inches: float
    Ram: int
    OS: str
    Weight: float
    Screen: str
    ScreenW: int
    ScreenH: int
    Touchscreen: int
    IPSpanel: int
    RetinaDisplay: int
    CPU_company: str
    CPU_freq: float
    CPU_model: str
    PrimaryStorage: int
    SecondaryStorage: int
    PrimaryStorageType: str
    SecondaryStorageType: str
    GPU_company: str
    GPU_model: str

    def get_data_as_dataframe(self) -> pd.DataFrame:
        """
        Convert input data into a pandas DataFrame.
        """

        try:
            return pd.DataFrame(
                {
                    "Company": [self.Company],
                    "Product": [self.Product],
                    "TypeName": [self.TypeName],
                    "Inches": [self.Inches],
                    "Ram": [self.Ram],
                    "OS": [self.OS],
                    "Weight": [self.Weight],
                    "Screen": [self.Screen],
                    "ScreenW": [self.ScreenW],
                    "ScreenH": [self.ScreenH],
                    "Touchscreen": [self.Touchscreen],
                    "IPSpanel": [self.IPSpanel],
                    "RetinaDisplay": [self.RetinaDisplay],
                    "CPU_company": [self.CPU_company],
                    "CPU_freq": [self.CPU_freq],
                    "CPU_model": [self.CPU_model],
                    "PrimaryStorage": [self.PrimaryStorage],
                    "SecondaryStorage": [self.SecondaryStorage],
                    "PrimaryStorageType": [self.PrimaryStorageType],
                    "SecondaryStorageType": [self.SecondaryStorageType],
                    "GPU_company": [self.GPU_company],
                    "GPU_model": [self.GPU_model],
                }
            )

        except Exception as e:
            logger.exception("Failed to create DataFrame.")
            raise CustomException(e, sys) from e
