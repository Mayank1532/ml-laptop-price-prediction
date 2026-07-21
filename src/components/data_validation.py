import sys

import pandas as pd

from src.config import DataValidationConfig
from src.constants import TARGET_COLUMN
from src.exception import CustomException
from src.logger import logger
from src.utils import read_yaml


class DataValidation:
    def __init__(self):
        self.config = DataValidationConfig()

    def validate(self) -> bool:
        try:
            logger.info("=" * 60)
            logger.info("Starting Data Validation")

            df = pd.read_csv(self.config.raw_data_path)

            schema = read_yaml(self.config.schema_path)

            expected_columns = schema["columns"]

            logger.info("Checking if dataset is empty...")

            if df.empty:
                raise ValueError("Dataset is empty.")

            logger.info("Checking required columns...")

            missing_columns = [col for col in expected_columns if col not in df.columns]

            if missing_columns:
                raise ValueError(f"Missing columns: {missing_columns}")

            logger.info("Checking duplicate columns...")

            if df.columns.duplicated().any():
                raise ValueError("Duplicate columns found.")

            logger.info("Checking target column...")

            if TARGET_COLUMN not in df.columns:
                raise ValueError(f"Target column '{TARGET_COLUMN}' missing.")

            logger.info("Data Validation Completed Successfully.")
            logger.info("=" * 60)

            return True

        except Exception as e:
            logger.exception("Data Validation Failed.")
            raise CustomException(e, sys) from e
