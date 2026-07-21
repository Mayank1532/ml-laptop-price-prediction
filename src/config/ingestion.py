from dataclasses import dataclass
from pathlib import Path

from .paths import EXTERNAL_DATA_DIR, RAW_DATA_DIR


@dataclass(frozen=True)
class DataIngestionConfig:
    dataset_path: Path = EXTERNAL_DATA_DIR / "laptop_prices.csv"
    raw_data_dir: Path = RAW_DATA_DIR
    raw_data_path: Path = RAW_DATA_DIR / "laptop_prices.csv"
