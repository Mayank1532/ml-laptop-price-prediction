from dataclasses import dataclass
from pathlib import Path

from src.logger import logger


logger.info("Initializing project configuration...")

# Project Root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Data Paths
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
EXTERNAL_DATA_DIR = DATA_DIR / "external"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Artifact Paths
ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"
MODEL_DIR = ARTIFACTS_DIR / "models"

# Log Path
LOG_DIR = PROJECT_ROOT / "logs"

# Create required directories
for directory in [
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    ARTIFACTS_DIR,
    MODEL_DIR,
    LOG_DIR,
]:
    directory.mkdir(parents=True, exist_ok=True)
    logger.info(f"Verified directory: {directory}")


@dataclass(frozen=True)
class DataIngestionConfig:
    dataset_path: Path = EXTERNAL_DATA_DIR / "laptop_prices.csv"
    raw_data_dir: Path = RAW_DATA_DIR
    raw_data_path: Path = RAW_DATA_DIR / "laptop_prices.csv"


@dataclass(frozen=True)
class ModelTrainerConfig:
    trained_model_path: Path = MODEL_DIR / "model.pkl"

@dataclass(frozen=True)
class DataValidationConfig:
    raw_data_path: Path = RAW_DATA_DIR / "laptop_prices.csv"
    schema_path: Path = PROJECT_ROOT / "config" / "schema.yaml"


logger.info("Project configuration initialized successfully.")