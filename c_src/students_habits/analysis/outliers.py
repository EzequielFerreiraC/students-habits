"""Detecção simples de outliers via IQR."""

from __future__ import annotations

import pandas as pd


def iqr_bounds(series: pd.Series, k: float = 1.5) -> tuple[float, float]:
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    return q1 - k * iqr, q3 + k * iqr


def detect_outliers(df: pd.DataFrame, column: str, k: float = 1.5) -> pd.DataFrame:
    low, high = iqr_bounds(df[column], k)
    mask = (df[column] < low) | (df[column] > high)
    return df.loc[mask]
