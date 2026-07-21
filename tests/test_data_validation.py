from src.components import DataValidation
from src.logger import logger


def test_data_validation():
    logger.info("=" * 60)
    logger.info("Starting Data Validation Test")

    validator = DataValidation()

    assert validator.validate() is True

    logger.info("Data Validation Test Passed")
    logger.info("=" * 60)
