from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
EXTERNAL_DATA_DIR = DATA_DIR / "external"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"
MODEL_DIR = ARTIFACTS_DIR / "models"

LOG_DIR = PROJECT_ROOT / "logs"

for directory in [
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    ARTIFACTS_DIR,
    MODEL_DIR,
    LOG_DIR,
]:
    directory.mkdir(parents=True, exist_ok=True)
