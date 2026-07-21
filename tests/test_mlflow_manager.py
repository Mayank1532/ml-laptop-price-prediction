from src.mlflow.mlflow_manager import MLflowManager


def test_mlflow_manager():
    manager = MLflowManager("Laptop Price Prediction")

    with manager.start_run():
        pass

    assert True
