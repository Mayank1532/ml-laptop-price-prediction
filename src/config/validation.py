from dataclasses import dataclass
from pathlib import Path

from .paths import PROJECT_ROOT, RAW_DATA_DIR


@dataclass(frozen=True)
class DataValidationConfig:
    raw_data_path: Path = RAW_DATA_DIR / "laptop_prices.csv"
    schema_path: Path = PROJECT_ROOT / "config" / "schema.yaml"
