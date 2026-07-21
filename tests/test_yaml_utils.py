from pathlib import Path

from src.logger import logger
from src.utils import read_yaml, write_yaml


def test_yaml_utils():
    logger.info("=" * 60)
    logger.info("Starting YAML Utils Test")

    test_file = Path("artifacts/test/config.yaml")

    sample_config = {
        "model": {
            "name": "RandomForest",
            "n_estimators": 100,
        },
        "training": {
            "test_size": 0.2,
            "random_state": 42,
        },
    }

    write_yaml(test_file, sample_config)

    loaded_config = read_yaml(test_file)

    assert loaded_config == sample_config

    logger.info("YAML Utils Test Passed Successfully")
    logger.info("=" * 60)
