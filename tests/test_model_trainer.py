from sklearn.linear_model import LinearRegression

from src.components import DataTransformation, ModelTrainer
from src.config import DataTransformationConfig, ModelTrainerConfig
from src.entity import ModelEvaluationResult
from src.utils import load_pickle


def test_model_trainer_initialization():
    config = ModelTrainerConfig()

    trainer = ModelTrainer(config)

    assert trainer.config == config


def test_get_models():
    trainer = ModelTrainer(ModelTrainerConfig())

    models = trainer._get_models()

    assert isinstance(models, dict)
    assert len(models) > 0
    assert "Linear Regression" in models
    assert "Random Forest" in models


def test_evaluate_models():
    transformer = DataTransformation(DataTransformationConfig())

    artifact = transformer.initiate_data_transformation()

    trainer = ModelTrainer(ModelTrainerConfig())

    models = trainer._get_models()

    results = trainer._evaluate_models(
        models=models,
        X_train=artifact.X_train,
        y_train=artifact.y_train,
        X_test=artifact.X_test,
        y_test=artifact.y_test,
    )

    assert isinstance(results, dict)
    assert len(results) > 0

    assert "Linear Regression" in results

    result = results["Linear Regression"]

    assert isinstance(result, ModelEvaluationResult)
    assert result.model is not None
    assert isinstance(result.r2, float)
    assert isinstance(result.mae, float)
    assert isinstance(result.rmse, float)


def test_select_best_model():
    transformer = DataTransformation(DataTransformationConfig())

    artifact = transformer.initiate_data_transformation()

    trainer = ModelTrainer(ModelTrainerConfig())

    models = trainer._get_models()

    results = trainer._evaluate_models(
        models=models,
        X_train=artifact.X_train,
        y_train=artifact.y_train,
        X_test=artifact.X_test,
        y_test=artifact.y_test,
    )

    name, model, result = trainer._select_best_model(
        evaluation_results=results,
    )

    assert isinstance(name, str)
    assert model is not None

    assert isinstance(result, ModelEvaluationResult)

    assert isinstance(result.r2, float)
    assert isinstance(result.mae, float)
    assert isinstance(result.rmse, float)


def test_save_model(tmp_path):
    trainer = ModelTrainer(
        ModelTrainerConfig(
            trained_model_path=tmp_path / "model.pkl",
            random_state=42,
        )
    )

    model = trainer._get_models()["Linear Regression"]

    trainer._save_model(model)

    assert (tmp_path / "model.pkl").exists()

    loaded_model = load_pickle(tmp_path / "model.pkl")

    assert isinstance(loaded_model, LinearRegression)


def test_initiate_model_trainer():
    transformer = DataTransformation(DataTransformationConfig())

    transformation_artifact = transformer.initiate_data_transformation()

    trainer = ModelTrainer(ModelTrainerConfig())

    trainer_artifact = trainer.initiate_model_trainer(transformation_artifact)

    print("Training completed")

    assert trainer_artifact.model_path.exists()
    assert trainer_artifact.model_name != ""
    assert trainer_artifact.train_r2_score is not None
    assert trainer_artifact.test_r2_score is not None
