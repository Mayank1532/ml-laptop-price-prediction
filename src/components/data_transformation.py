import sys

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.config import DataTransformationConfig
from src.constants import (
    CATEGORICAL_COLUMNS,
    NUMERICAL_COLUMNS,
    TARGET_COLUMN,
)
from src.entity import DataTransformationArtifact
from src.exception import CustomException
from src.logger import logger
from src.utils import save_pickle


class DataTransformation:
    """
    Prepare the dataset for model training.

    Responsibilities:
    - Load the raw dataset
    - Split features and target
    - Perform train/test split
    - Build preprocessing pipelines
    - Transform training and testing data
    - Save the fitted preprocessor
    """

    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def _load_dataset(self) -> pd.DataFrame:
        """
        Load dataset from the configured input path.
        """
        try:
            logger.info(f"Loading dataset from: {self.config.input_data_path}")

            df = pd.read_csv(self.config.input_data_path)

            logger.info("Dataset loaded successfully.")

            return df

        except Exception as e:
            logger.exception("Failed to load dataset.")
            raise CustomException(e, sys) from e

    def _split_features_target(
        self,
        df: pd.DataFrame,
    ) -> tuple[pd.DataFrame, pd.Series]:
        """
        Split dataset into features (X) and target (y).
        """
        try:
            logger.info("Splitting dataset into features and target...")

            X = df.drop(columns=[TARGET_COLUMN])
            y = df[TARGET_COLUMN]

            logger.info(f"Feature matrix shape : {X.shape}")
            logger.info(f"Target vector shape  : {y.shape}")

            return X, y

        except Exception as e:
            logger.exception("Failed to split features and target.")
            raise CustomException(e, sys) from e

    def _train_test_split(
        self,
        X: pd.DataFrame,
        y: pd.Series,
    ) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
        """
        Split features and target into training and testing sets.
        """
        try:
            logger.info("Performing train-test split...")

            X_train, X_test, y_train, y_test = train_test_split(
                X,
                y,
                test_size=self.config.test_size,
                random_state=self.config.random_state,
            )

            logger.info(f"X_train shape : {X_train.shape}")
            logger.info(f"X_test shape  : {X_test.shape}")
            logger.info(f"y_train shape : {y_train.shape}")
            logger.info(f"y_test shape  : {y_test.shape}")

            return X_train, X_test, y_train, y_test

        except Exception as e:
            logger.exception("Failed during train-test split.")
            raise CustomException(e, sys) from e

    def _build_preprocessor(self) -> ColumnTransformer:
        """
        Build preprocessing pipeline.
        """
        try:
            logger.info("Building preprocessing pipeline...")

            numerical_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler()),
                ]
            )

            categorical_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    (
                        "encoder",
                        OneHotEncoder(
                            handle_unknown="ignore",
                            sparse_output=False,
                        ),
                    ),
                ]
            )

            preprocessor = ColumnTransformer(
                transformers=[
                    (
                        "numerical",
                        numerical_pipeline,
                        NUMERICAL_COLUMNS,
                    ),
                    (
                        "categorical",
                        categorical_pipeline,
                        CATEGORICAL_COLUMNS,
                    ),
                ]
            )

            logger.info("Preprocessing pipeline created successfully.")

            return preprocessor

        except Exception as e:
            logger.exception("Failed to build preprocessing pipeline.")
            raise CustomException(e, sys) from e

    def _transform_features(
        self,
        preprocessor: ColumnTransformer,
        X_train: pd.DataFrame,
        X_test: pd.DataFrame,
    ) -> tuple:
        """
        Fit the preprocessor on training data and transform both
        training and testing features.
        """
        try:
            logger.info("Transforming training and testing features...")

            X_train_processed = preprocessor.fit_transform(X_train)

            X_test_processed = preprocessor.transform(X_test)

            logger.info(f"Processed X_train shape : {X_train_processed.shape}")

            logger.info(f"Processed X_test shape : {X_test_processed.shape}")

            return X_train_processed, X_test_processed

        except Exception as e:
            logger.exception("Feature transformation failed.")
            raise CustomException(e, sys) from e

    def _save_preprocessor(
        self,
        preprocessor: ColumnTransformer,
    ) -> None:
        """
        Save the fitted preprocessor to disk.
        """
        try:
            logger.info(f"Saving preprocessor to: {self.config.preprocessor_path}")

            save_pickle(
                file_path=self.config.preprocessor_path,
                obj=preprocessor,
            )

            logger.info("Preprocessor saved successfully.")

        except Exception as e:
            logger.exception("Failed to save preprocessor.")
            raise CustomException(e, sys) from e

    def initiate_data_transformation(
        self,
    ) -> DataTransformationArtifact:
        """
        Main entry point for data transformation.
        """
        try:
            logger.info("=" * 60)
            logger.info("Starting Data Transformation")

            df = self._load_dataset()

            X, y = self._split_features_target(df)

            X_train, X_test, y_train, y_test = self._train_test_split(X, y)

            preprocessor = self._build_preprocessor()

            X_train_processed, X_test_processed = self._transform_features(
                preprocessor,
                X_train,
                X_test,
            )

            self._save_preprocessor(preprocessor)

            logger.info("Data Transformation skeleton executed successfully.")
            logger.info("=" * 60)

            return DataTransformationArtifact(
                X_train=X_train_processed,
                X_test=X_test_processed,
                y_train=y_train,
                y_test=y_test,
                preprocessor=preprocessor,
            )
        except Exception as e:
            logger.exception("Data Transformation failed.")
            raise CustomException(e, sys) from e
