from dataclasses import dataclass

import numpy as np
from sklearn.compose import ColumnTransformer


@dataclass(frozen=True)
class DataTransformationArtifact:
    X_train: np.ndarray
    X_test: np.ndarray
    y_train: np.ndarray
    y_test: np.ndarray
    preprocessor: ColumnTransformer
