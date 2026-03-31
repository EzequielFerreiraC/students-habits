"""Codificação de variáveis categóricas."""

from __future__ import annotations

import pandas as pd

ORDINAL_DIET = {"Poor": 0, "Fair": 1, "Good": 2}
ORDINAL_INTERNET = {"Poor": 0, "Average": 1, "Good": 2}
BINARY_YESNO = {"No": 0, "Yes": 1}


def encode_dataset(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    if "diet_quality" in out:
        out["diet_quality_ord"] = out["diet_quality"].map(ORDINAL_DIET)
    if "internet_quality" in out:
        out["internet_quality_ord"] = out["internet_quality"].map(ORDINAL_INTERNET)
    for col in ("part_time_job", "extracurricular_participation"):
        if col in out:
            out[f"{col}_bin"] = out[col].map(BINARY_YESNO)
    return out
