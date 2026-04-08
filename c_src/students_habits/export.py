"""Helpers de exportação para saídas de análise."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from .paths import OUTPUT_DIR


def export_dataframe(df: pd.DataFrame, name: str) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUTPUT_DIR / f"{name}.csv"
    df.to_csv(out, index=False)
    return out
