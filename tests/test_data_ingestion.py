from src.components import DataIngestion
from src.logger import logger


def test_data_ingestion():
    logger.info("=" * 60)
    logger.info("Starting Data Ingestion Test")

    ingestion = DataIngestion()

    raw_file = ingestion.initiate_data_ingestion()

    assert raw_file.exists()

    logger.info(f"Raw dataset saved at: {raw_file}")

    logger.info("Data Ingestion Test Passed")
    logger.info("=" * 60)
