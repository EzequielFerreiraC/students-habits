"""Classifica estudantes pela nota do exame."""

from __future__ import annotations

import pandas as pd

LABELS = ["Low", "Medium", "High", "Excellent"]
BINS = [-0.1, 50, 70, 85, 100.1]


def add_performance_label(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["performance"] = pd.cut(out["exam_score"], bins=BINS, labels=LABELS)
    return out
