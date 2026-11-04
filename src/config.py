from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"
MODELS_DIR = ROOT / "models"
REPORTS_DIR = ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"
DATASET_PATH = PROCESSED_DIR / "dataset.parquet"


def load_config() -> dict:
    with open(ROOT / "config.yaml", encoding="utf-8") as file:
        return yaml.safe_load(file)


def ensure_dirs() -> None:
    for path in (RAW_DIR, PROCESSED_DIR, MODELS_DIR, REPORTS_DIR, FIGURES_DIR):
        path.mkdir(parents=True, exist_ok=True)