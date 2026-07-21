import sys
from pathlib import Path
from typing import Any, cast

import yaml

from src.exception import CustomException
from src.logger import logger


def read_yaml(file_path: Path | str) -> dict[str, Any]:
    """
    Read a YAML file and return its contents as a dictionary.
    """
    try:
        file_path = Path(file_path)

        logger.info(f"Reading YAML file: {file_path}")
        with open(file_path, encoding="utf-8") as yaml_file:
            content = yaml.safe_load(yaml_file) or {}

        return cast(dict[str, Any], content)

    except Exception as e:
        logger.exception("Failed to read YAML file.")
        raise CustomException(e, sys) from e


def write_yaml(file_path: Path | str, data: dict[str, Any]) -> None:
    """
    Write a dictionary to a YAML file.
    """
    try:
        file_path = Path(file_path)

        file_path.parent.mkdir(parents=True, exist_ok=True)

        logger.info(f"Writing YAML file: {file_path}")

        with open(file_path, "w", encoding="utf-8") as yaml_file:
            yaml.safe_dump(
                data,
                yaml_file,
                sort_keys=False,
                default_flow_style=False,
            )

        logger.info("YAML file written successfully.")

    except Exception as e:
        logger.exception("Failed to write YAML file.")
        raise CustomException(e, sys) from e
