import sys

import pytest

from src.exception import CustomException
from src.logger import logger


def test_exception():
    logger.info("=" * 60)
    logger.info("Starting Exception Module Test")

    with pytest.raises(CustomException):
        try:
            logger.info("Generating ZeroDivisionError...")
            _ = 10 / 0

        except Exception as e:
            logger.exception("Exception captured successfully.")
            raise CustomException(e, sys) from e

    logger.info("Exception Module Test Completed Successfully")
    logger.info("=" * 60)
