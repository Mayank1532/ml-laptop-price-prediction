from src.config import (
    ARTIFACTS_DIR,
    DATA_DIR,
    EXTERNAL_DATA_DIR,
    LOG_DIR,
    MODEL_DIR,
    PROCESSED_DATA_DIR,
    PROJECT_ROOT,
    RAW_DATA_DIR,
    DataIngestionConfig,
)
from src.logger import logger


def test_configuration():
    logger.info("=" * 60)
    logger.info("Starting Configuration Module Test")

    config = DataIngestionConfig()

    print("\nProject Configuration\n")

    print(f"PROJECT_ROOT      : {PROJECT_ROOT}")
    print(f"DATA_DIR          : {DATA_DIR}")
    print(f"RAW_DATA_DIR      : {RAW_DATA_DIR}")
    print(f"EXTERNAL_DATA_DIR : {EXTERNAL_DATA_DIR}")
    print(f"PROCESSED_DATA_DIR: {PROCESSED_DATA_DIR}")
    print(f"ARTIFACTS_DIR     : {ARTIFACTS_DIR}")
    print(f"MODEL_DIR         : {MODEL_DIR}")
    print(f"LOG_DIR           : {LOG_DIR}")

    print("\nData Ingestion Configuration\n")

    print(f"Dataset Path : {config.dataset_path}")
    print(f"Raw Data Path: {config.raw_data_path}")

    logger.info("Configuration Module Tested Successfully")
    logger.info("=" * 60)


if __name__ == "__main__":
    test_configuration()
