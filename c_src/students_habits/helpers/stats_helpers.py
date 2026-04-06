"""Helpers pequenos compartilhados entre módulos de estatísticas."""

from __future__ import annotations

import pandas as pd


def safe_mean(series: pd.Series) -> float:
    return float(series.dropna().mean()) if len(series.dropna()) else 0.0


def safe_std(series: pd.Series) -> float:
    return float(series.dropna().std(ddof=0)) if len(series.dropna()) else 0.0
