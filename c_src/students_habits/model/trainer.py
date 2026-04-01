"""Treina uma regressão linear baseline no dataset codificado."""

from __future__ import annotations

import numpy as np
import pandas as pd

FEATURES = [
    "study_hours_per_day",
    "sleep_hours",
    "social_media_hours",
    "netflix_hours",
    "exercise_frequency",
    "attendance_percentage",
    "mental_health_rating",
]


def _design_matrix(df: pd.DataFrame) -> np.ndarray:
    x = df[FEATURES].to_numpy(dtype=float)
    return np.column_stack([np.ones(len(x)), x])


def train(df: pd.DataFrame) -> np.ndarray:
    """Resolve as equações normais e retorna os coeficientes."""
    x = _design_matrix(df)
    y = df["exam_score"].to_numpy(dtype=float)
    coefficients, *_ = np.linalg.lstsq(x, y, rcond=None)
    return coefficients
