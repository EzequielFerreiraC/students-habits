"""Utilitários de correlação."""

from __future__ import annotations

import pandas as pd


def correlation_matrix(df: pd.DataFrame) -> pd.DataFrame:
    return df.select_dtypes(include="number").corr()


def correlations_with(df: pd.DataFrame, column: str = "exam_score") -> pd.Series:
    return (
        correlation_matrix(df)[column]
        .drop(labels=[column])
        .sort_values(ascending=False)
    )
