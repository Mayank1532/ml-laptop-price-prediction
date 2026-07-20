from dataclasses import dataclass
from pathlib import Path

from .paths import MODEL_DIR

@dataclass(frozen=True)
class ModelTrainerConfig:
    trained_model_path: Path = MODEL_DIR / "model.pkl"