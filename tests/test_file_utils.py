from pathlib import Path

from src.logger import logger
from src.utils import (
    create_directories,
    load_pickle,
    save_pickle,
)


def test_file_utils():
    logger.info("=" * 60)
    logger.info("Starting File Utils Test")

    test_dir = Path("artifacts/test")
    test_file = test_dir / "sample.pkl"

    create_directories(test_dir)

    sample_data = {
        "model": "RandomForest",
        "accuracy": 0.95,
    }

    save_pickle(test_file, sample_data)

    loaded_data = load_pickle(test_file)

    assert loaded_data == sample_data

    logger.info("File Utils Test Passed Successfully")
    logger.info("=" * 60)
