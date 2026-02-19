"""Helpers de limpeza para o dataset."""

from __future__ import annotations

import pandas as pd

NUMERIC_COLUMNS = [
    "age",
    "study_hours_per_day",
    "social_media_hours",
    "netflix_hours",
    "attendance_percentage",
    "sleep_hours",
    "exercise_frequency",
    "mental_health_rating",
    "exam_score",
]


def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates(subset="student_id", keep="first")


def fill_numeric_missing(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    for col in NUMERIC_COLUMNS:
        if col in out.columns:
            out[col] = out[col].fillna(out[col].median())
    return out


def normalize_strings(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    for col in out.select_dtypes(include="object").columns:
        out[col] = out[col].astype(str).str.strip()
    return out


def clean(df: pd.DataFrame) -> pd.DataFrame:
    return normalize_strings(fill_numeric_missing(drop_duplicates(df)))
