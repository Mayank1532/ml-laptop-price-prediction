import sys
from typing import Any

import mlflow.sklearn
import pandas as pd
from mlflow.models import infer_signature
from sklearn.ensemble import (
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import (
    Lasso,
    LinearRegression,
    Ridge,
)
from sklearn.metrics import (
    mean_absolute_error,
    r2_score,
    root_mean_squared_error,
)
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeRegressor

from src.config import ModelTrainerConfig
from src.entity import (
    DataTransformationArtifact,
    ModelEvaluationResult,
    ModelTrainerArtifact,
)
from src.exception import CustomException
from src.logger import logger
from src.mlflow.mlflow_manager import MLflowManager
from src.utils import save_pickle


class ModelTrainer:
    """
    Handles model training, hyperparameter tuning,
    evaluation and persistence.
    """

    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    ###########################################################################
    # Models
    ###########################################################################

    def _get_models(self) -> dict[str, Any]:
        """
        Return regression models.
        """
        try:
            logger.info("Initializing regression models...")

            return {
                "Linear Regression": LinearRegression(),
                "Ridge": Ridge(),
                "Lasso": Lasso(
                    max_iter=10000,
                ),
                "Decision Tree": DecisionTreeRegressor(
                    random_state=self.config.random_state,
                ),
                "Random Forest": RandomForestRegressor(
                    random_state=self.config.random_state,
                ),
                "Gradient Boosting": GradientBoostingRegressor(
                    random_state=self.config.random_state,
                ),
            }

        except Exception as e:
            logger.exception("Model initialization failed.")
            raise CustomException(e, sys) from e

    ###########################################################################
    # Hyperparameters
    ###########################################################################

    def _get_model_params(self) -> dict[str, dict]:
        """
        Hyperparameter search space.
        """

        return {
            "Linear Regression": {},
            "Ridge": {
                "alpha": [0.1, 1.0, 10.0],
            },
            "Lasso": {
                "alpha": [0.001, 0.01, 0.1, 1.0],
            },
            "Decision Tree": {
                "max_depth": [5, 10, 20],
                "min_samples_split": [2, 5, 10],
            },
            "Random Forest": {
                "n_estimators": [100, 200],
                "max_depth": [10, 20],
                "min_samples_split": [2, 5],
            },
            "Gradient Boosting": {
                "learning_rate": [0.01, 0.1],
                "n_estimators": [100, 200],
                "max_depth": [3, 5],
            },
        }

    ###########################################################################
    # Hyperparameter Tuning
    ###########################################################################

    def _tune_model(
        self,
        model,
        parameter_grid: dict,
        X_train,
        y_train,
    ):
        """
        Tune a single model using GridSearchCV.
        """

        try:

            if not parameter_grid:

                logger.info(
                    "No hyperparameters defined for %s.",
                    model.__class__.__name__,
                )

                model.fit(
                    X_train,
                    y_train,
                )

                return model

            logger.info(
                "Running GridSearchCV for %s",
                model.__class__.__name__,
            )

            grid_search = GridSearchCV(
                estimator=model,
                param_grid=parameter_grid,
                cv=5,
                scoring="r2",
                n_jobs=-1,
            )

            grid_search.fit(
                X_train,
                y_train,
            )

            logger.info(
                "Best Parameters: %s",
                grid_search.best_params_,
            )

            logger.info(
                "Best CV Score: %.4f",
                grid_search.best_score_,
            )

            return grid_search.best_estimator_

        except Exception as e:
            logger.exception("Hyperparameter tuning failed.")
            raise CustomException(e, sys) from e

    ###########################################################################
    # Model Evaluation
    ###########################################################################

    def _evaluate_models(
        self,
        models: dict[str, Any],
        X_train,
        y_train,
        X_test,
        y_test,
    ) -> dict[str, ModelEvaluationResult]:
        """
        Tune and evaluate all models.
        """

        try:
            logger.info("Evaluating regression models...")

            evaluation_results = {}

            parameter_grids = self._get_model_params()

            for model_name, model in models.items():

                logger.info("=" * 80)
                logger.info("Training %s", model_name)

                tuned_model = self._tune_model(
                    model=model,
                    parameter_grid=parameter_grids[model_name],
                    X_train=X_train,
                    y_train=y_train,
                )

                predictions = tuned_model.predict(X_test)

                r2 = r2_score(
                    y_test,
                    predictions,
                )

                mae = mean_absolute_error(
                    y_test,
                    predictions,
                )

                rmse = root_mean_squared_error(
                    y_test,
                    predictions,
                )

                evaluation_results[model_name] = ModelEvaluationResult(
                    model=tuned_model,
                    r2=r2,
                    mae=mae,
                    rmse=rmse,
                )
                logger.info(
                    "%s | R²: %.4f | MAE: %.4f | RMSE: %.4f",
                    model_name,
                    r2,
                    mae,
                    rmse,
                )

            logger.info("=" * 80)
            logger.info("All models evaluated successfully.")

            return evaluation_results

        except Exception as e:
            logger.exception("Model evaluation failed.")
            raise CustomException(e, sys) from e

    ###########################################################################
    # Best Model Selection
    ###########################################################################

    def _select_best_model(
        self,
        evaluation_results: dict[str, ModelEvaluationResult],
    ) -> tuple[str, Any, ModelEvaluationResult]:
        """
        Select the best model using R² score.
        """

        try:

            logger.info("Selecting best model...")

            best_model_name = max(
                evaluation_results,
                key=lambda x: evaluation_results[x].r2,
            )

            best_result = evaluation_results[best_model_name]

            best_model = best_result.model
            best_metrics = {
                "r2": best_result.r2,
                "mae": best_result.mae,
                "rmse": best_result.rmse,
            }

            logger.info(
                "Best Model : %s",
                best_model_name,
            )

            logger.info(
                "Best Test R² : %.4f",
                best_metrics["r2"],
            )

            return (
                best_model_name,
                best_model,
                best_result,
            )

        except Exception as e:
            logger.exception("Best model selection failed.")
            raise CustomException(e, sys) from e

            ###########################################################################

    # Save Model
    ###########################################################################

    def _save_model(
        self,
        model,
    ) -> None:
        """
        Save the trained model.
        """

        try:

            logger.info(
                "Saving model to %s",
                self.config.trained_model_path,
            )

            save_pickle(
                file_path=self.config.trained_model_path,
                obj=model,
            )

            logger.info("Model saved successfully.")

        except Exception as e:
            logger.exception("Failed to save model.")
            raise CustomException(e, sys) from e

    ###########################################################################
    # Model Training Pipeline
    ###########################################################################

    def initiate_model_trainer(
        self,
        artifact: DataTransformationArtifact,
    ) -> ModelTrainerArtifact:
        """
        Complete model training pipeline.
        """

        try:

            logger.info("=" * 100)
            logger.info("Starting Model Trainer Pipeline")
            logger.info("=" * 100)

            ############################################################
            # Load Models
            ############################################################

            models = self._get_models()

            ############################################################
            # Evaluate Models
            ############################################################

            evaluation_results = self._evaluate_models(
                models=models,
                X_train=artifact.X_train,
                y_train=artifact.y_train,
                X_test=artifact.X_test,
                y_test=artifact.y_test,
            )

            ############################################################
            # Select Best Model
            ############################################################

            (
                best_model_name,
                best_model,
                best_result,
            ) = self._select_best_model(
                evaluation_results=evaluation_results,
            )

            ############################################################
            # Calculate Training Score
            ############################################################

            train_predictions = best_model.predict(
                artifact.X_train,
            )

            train_r2 = r2_score(
                artifact.y_train,
                train_predictions,
            )

            ############################################################
            # Save Best Model
            ############################################################

            self._save_model(best_model)

            ############################################################
            # MLflow Logging
            ############################################################

            mlflow_manager = MLflowManager("Laptop Price Prediction")

            with mlflow_manager.start_run(run_name=best_model_name):

                mlflow_manager.log_params(
                    {
                        "model": best_model_name,
                    }
                )

            mlflow_manager.log_metrics(
                {
                    "train_r2": train_r2,
                    "test_r2": best_result.r2,
                    "mae": best_result.mae,
                    "rmse": best_result.rmse,
                }
            )
            # ===========================
            # Log model to MLflow
            # ===========================

            input_example = pd.DataFrame(
                artifact.X_train[:5],
            )

            signature = infer_signature(
                artifact.X_train,
                train_predictions,
            )

            mlflow.sklearn.log_model(
                sk_model=best_model,
                name="model",
                signature=signature,
                input_example=input_example,
            )

            run = mlflow.active_run()

            mlflow_manager.register_model(
                model_uri=f"runs:/{run.info.run_id}/model",
                model_name="LaptopPricePrediction",
            )

            ############################################################
            # Build Artifact
            ############################################################

            trainer_artifact = ModelTrainerArtifact(
                model_path=self.config.trained_model_path,
                model_name=best_model_name,
                train_r2_score=train_r2,
                test_r2_score=best_result.r2,
            )

            logger.info("Training completed successfully.")
            logger.info("Best Model : %s", best_model_name)
            logger.info("Train R² : %.4f", train_r2)
            logger.info("Test R² : %.4f", best_result.r2)
            logger.info("=" * 100)

            return trainer_artifact

        except Exception as e:
            logger.exception("Model training pipeline failed.")
            raise CustomException(e, sys) from e
