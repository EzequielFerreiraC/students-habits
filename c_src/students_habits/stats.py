"""Estatísticas descritivas do dataset."""

from __future__ import annotations

import pandas as pd


def numeric_summary(df: pd.DataFrame) -> pd.DataFrame:
    return df.describe().T


def group_means(df: pd.DataFrame, by: str, column: str) -> pd.Series:
    return df.groupby(by)[column].mean().sort_values(ascending=False)


def top_performers(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    return df.nlargest(n, "exam_score")
