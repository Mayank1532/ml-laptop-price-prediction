import shutil
import sys
from pathlib import Path

from src.config import DataIngestionConfig
from src.exception import CustomException
from src.logger import logger
from src.utils import create_directories


class DataIngestion:
    """
    Handles copying the source dataset into the raw data directory.
    """

    def __init__(self):
        self.config = DataIngestionConfig()

    def initiate_data_ingestion(self) -> Path:
        try:
            logger.info("=" * 60)
            logger.info("Starting Data Ingestion")

            source_file = self.config.dataset_path

            logger.info(f"Checking dataset: {source_file}")

            if not source_file.exists():
                raise FileNotFoundError(f"Dataset not found: {source_file}")

            create_directories(self.config.raw_data_dir)

            logger.info("Copying dataset to raw directory...")

            shutil.copy2(
                source_file,
                self.config.raw_data_path,
            )

            logger.info(f"Dataset copied successfully to: {self.config.raw_data_path}")

            logger.info("Data Ingestion Completed Successfully")
            logger.info("=" * 60)

            return self.config.raw_data_path

        except Exception as e:
            logger.exception("Error occurred during Data Ingestion.")
            raise CustomException(e, sys) from e
