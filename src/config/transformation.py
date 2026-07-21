from dataclasses import dataclass
from pathlib import Path

from src.constants import RANDOM_STATE, TEST_SIZE

from .paths import MODEL_DIR, RAW_DATA_DIR


@dataclass(frozen=True)
class DataTransformationConfig:
    input_data_path: Path = RAW_DATA_DIR / "laptop_prices.csv"
    preprocessor_path: Path = MODEL_DIR / "preprocessor.pkl"
    test_size: float = TEST_SIZE
    random_state: int = RANDOM_STATE
