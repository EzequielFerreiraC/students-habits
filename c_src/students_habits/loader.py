"""Utilitários de carregamento do dataset."""

from pathlib import Path

import pandas as pd

DEFAULT_PATH = Path("a_data/student_habits_performance.csv")


def load_dataset(path: str | Path | None = None) -> pd.DataFrame:
    """Carrega o dataset de hábitos como DataFrame."""
    csv_path = Path(path) if path else DEFAULT_PATH
    if not csv_path.exists():
        raise FileNotFoundError(f"Dataset não encontrado em {csv_path}")
    return pd.read_csv(csv_path)


def load_sample(n: int = 10, path: str | Path | None = None) -> pd.DataFrame:
    """Carrega apenas as primeiras ``n`` linhas, útil para inspeções rápidas."""
    return load_dataset(path).head(n)
