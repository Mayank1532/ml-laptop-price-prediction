from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ModelEvaluationResult:
    """
    Stores evaluation metrics and the trained model.
    """

    model: Any
    r2: float
    mae: float
    rmse: float
