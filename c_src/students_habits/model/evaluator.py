"""Avalia o modelo baseline."""

from __future__ import annotations

import numpy as np
import pandas as pd

from .trainer import FEATURES, _design_matrix


def predict(df: pd.DataFrame, coefficients: np.ndarray) -> np.ndarray:
    return _design_matrix(df) @ coefficients


def rmse(df: pd.DataFrame, coefficients: np.ndarray) -> float:
    preds = predict(df, coefficients)
    return float(np.sqrt(np.mean((df["exam_score"].to_numpy() - preds) ** 2)))


def r2(df: pd.DataFrame, coefficients: np.ndarray) -> float:
    y = df["exam_score"].to_numpy(dtype=float)
    preds = predict(df, coefficients)
    ss_res = float(np.sum((y - preds) ** 2))
    ss_tot = float(np.sum((y - y.mean()) ** 2))
    return 1 - ss_res / ss_tot if ss_tot > 0 else 0.0
