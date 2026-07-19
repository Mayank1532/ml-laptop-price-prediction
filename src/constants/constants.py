from src.logger import logger

logger.info("Loading project constants...")

# Dataset
TARGET_COLUMN = "Price_euros"

# Randomness
RANDOM_STATE = 42

# Train/Test Split
TEST_SIZE = 0.20

# Cross Validation
CV_FOLDS = 5

# File Names
MODEL_FILE_NAME = "model.pkl"
PREPROCESSOR_FILE_NAME = "preprocessor.pkl"

# Supported File Extensions
CSV_EXTENSION = ".csv"
PKL_EXTENSION = ".pkl"

logger.info("Project constants loaded successfully.")   