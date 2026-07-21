from pathlib import Path

from src.components import DataTransformation
from src.config import DataTransformationConfig
from src.entity import DataTransformationArtifact


def test_data_transformation_initialization():
    config = DataTransformationConfig()
    transformer = DataTransformation(config)

    assert transformer.config == config


def test_build_preprocessor():
    transformer = DataTransformation(DataTransformationConfig())

    preprocessor = transformer._build_preprocessor()

    assert preprocessor is not None


def test_split_features_target():
    transformer = DataTransformation(DataTransformationConfig())

    df = transformer._load_dataset()

    X, y = transformer._split_features_target(df)

    assert len(X.columns) > 0
    assert len(X) == len(y)


def test_train_test_split():
    transformer = DataTransformation(DataTransformationConfig())

    artifact = transformer.initiate_data_transformation()

    assert isinstance(artifact, DataTransformationArtifact)

    assert artifact.X_train is not None
    assert artifact.X_test is not None
    assert artifact.y_train is not None
    assert artifact.y_test is not None
    assert artifact.preprocessor is not None

    assert len(artifact.X_train) > 0
    assert len(artifact.X_test) > 0
    assert len(artifact.y_train) > 0
    assert len(artifact.y_test) > 0


def test_transform_features():
    transformer = DataTransformation(DataTransformationConfig())

    df = transformer._load_dataset()

    X, y = transformer._split_features_target(df)

    X_train, X_test, _, _ = transformer._train_test_split(X, y)

    preprocessor = transformer._build_preprocessor()

    X_train_processed, X_test_processed = transformer._transform_features(
        preprocessor,
        X_train,
        X_test,
    )

    assert X_train_processed.shape[0] == len(X_train)
    assert X_test_processed.shape[0] == len(X_test)


def test_save_preprocessor():
    transformer = DataTransformation(DataTransformationConfig())

    preprocessor = transformer._build_preprocessor()

    transformer._save_preprocessor(preprocessor)

    assert Path(transformer.config.preprocessor_path).exists()
