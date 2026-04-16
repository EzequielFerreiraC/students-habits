"""Utilitários de carregamento do dataset."""

from pathlib import Path

import pandas as pd

from .paths import DEFAULT_DATASET


def load_dataset(path: str | Path | None = None) -> pd.DataFrame:
    """Carrega o dataset de hábitos como DataFrame."""
    return pd.read_csv(Path(path) if path else DEFAULT_DATASET)


def load_sample(n: int = 10, path: str | Path | None = None) -> pd.DataFrame:
    """Carrega apenas as primeiras ``n`` linhas."""
    return load_dataset(path).head(n)
