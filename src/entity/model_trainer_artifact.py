from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ModelTrainerArtifact:
    model_path: Path
    model_name: str
    train_r2_score: float
    test_r2_score: float
