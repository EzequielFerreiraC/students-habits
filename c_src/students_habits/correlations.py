"""Utilitários de correlação."""

from __future__ import annotations

import pandas as pd


def correlation_matrix(df: pd.DataFrame) -> pd.DataFrame:
    numeric = df.select_dtypes(include="number")
    if numeric.empty:
        return pd.DataFrame()
    return numeric.corr()


def correlations_with(df: pd.DataFrame, column: str = "exam_score") -> pd.Series:
    corr = correlation_matrix(df)
    if corr.empty or column not in corr.columns:
        return pd.Series(dtype=float)
    return corr[column].drop(labels=[column]).sort_values(ascending=False)
