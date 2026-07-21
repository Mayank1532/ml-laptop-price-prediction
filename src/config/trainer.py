from dataclasses import dataclass
from pathlib import Path

from src.constants import MODEL_FILE_NAME, RANDOM_STATE

from .paths import MODEL_DIR


@dataclass(frozen=True)
class ModelTrainerConfig:
    """
    Configuration for model training.
    """

    trained_model_path: Path = MODEL_DIR / MODEL_FILE_NAME
    random_state: int = RANDOM_STATE
