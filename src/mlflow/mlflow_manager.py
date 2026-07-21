import mlflow.sklearn

import mlflow


class MLflowManager:

    def __init__(self, experiment_name: str):
        mlflow.set_experiment(experiment_name)

    def start_run(self, run_name=None):
        if mlflow.active_run():
            mlflow.end_run()
        return mlflow.start_run(run_name=run_name)

    @staticmethod
    def log_params(params):
        mlflow.log_params(params)

    @staticmethod
    def log_metrics(metrics):
        mlflow.log_metrics(metrics)

    def register_model(self, model_uri: str, model_name: str):
        mlflow.register_model(
            model_uri=model_uri,
            name=model_name,
        )
