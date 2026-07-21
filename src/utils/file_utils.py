import os
import pickle
import sys
from pathlib import Path
from typing import Any

from src.exception import CustomException
from src.logger import logger


def create_directories(*directories: Path | str) -> None:
    """
    Create one or more directories if they do not exist.
    """
    try:
        for directory in directories:
            directory = Path(directory)
            directory.mkdir(parents=True, exist_ok=True)
            logger.info(f"Verified directory exists: {directory}")

    except Exception as e:
        logger.exception("Error while creating directories.")
        raise CustomException(e, sys) from e


def save_pickle(file_path: Path | str, obj: Any) -> None:
    """
    Save any Python object as a pickle file.
    """
    try:
        file_path = Path(file_path)

        os.makedirs(file_path.parent, exist_ok=True)

        with open(file_path, "wb") as file:
            pickle.dump(obj, file)

        logger.info(f"Pickle file saved successfully: {file_path}")

    except Exception as e:
        logger.exception("Error while saving pickle file.")
        raise CustomException(e, sys) from e


def load_pickle(file_path: Path | str) -> Any:
    """
    Load a pickle object.
    """
    try:
        file_path = Path(file_path)

        with open(file_path, "rb") as file:
            obj = pickle.load(file)

        logger.info(f"Pickle file loaded successfully: {file_path}")

        return obj

    except Exception as e:
        logger.exception("Error while loading pickle file.")
        raise CustomException(e, sys) from e
