from src.constants import (
    CV_FOLDS,
    MODEL_FILE_NAME,
    PREPROCESSOR_FILE_NAME,
    RANDOM_STATE,
    TARGET_COLUMN,
    TEST_SIZE,
)
from src.logger import logger


def test_constants():
    logger.info("=" * 60)
    logger.info("Starting Constants Module Test")

    print("\nProject Constants\n")

    print(f"Target Column      : {TARGET_COLUMN}")
    print(f"Random State       : {RANDOM_STATE}")
    print(f"Test Size          : {TEST_SIZE}")
    print(f"CV Folds           : {CV_FOLDS}")
    print(f"Model File         : {MODEL_FILE_NAME}")
    print(f"Preprocessor File  : {PREPROCESSOR_FILE_NAME}")

    logger.info("Constants Module Tested Successfully")
    logger.info("=" * 60)


if __name__ == "__main__":
    test_constants()
