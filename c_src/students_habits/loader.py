"""Utilitários de carregamento do dataset."""

from pathlib import Path

import pandas as pd

from .paths import DEFAULT_DATASET


def load_dataset(path: str | Path | None = None) -> pd.DataFrame:
    csv_path = Path(path) if path else DEFAULT_DATASET
    if not csv_path.exists():
        raise FileNotFoundError(f"Dataset não encontrado em {csv_path}")
    return pd.read_csv(csv_path)


def load_sample(n: int = 10, path: str | Path | None = None) -> pd.DataFrame:
    return load_dataset(path).head(n)
