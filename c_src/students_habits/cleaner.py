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

CATEGORICAL_COLUMNS = [
    "gender",
    "part_time_job",
    "diet_quality",
    "parental_education_level",
    "internet_quality",
    "extracurricular_participation",
]


def normalize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out.columns = (
        out.columns.str.strip()
        .str.lower()
        .str.replace(r"[ \-]+", "_", regex=True)
    )
    return out


def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates(subset="student_id", keep="first")


def fill_numeric_missing(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    for col in NUMERIC_COLUMNS:
        if col in out.columns:
            out[col] = out[col].fillna(out[col].median())
    return out


def fill_categorical_missing(df: pd.DataFrame, fill: str = "Unknown") -> pd.DataFrame:
    out = df.copy()
    for col in CATEGORICAL_COLUMNS:
        if col in out.columns:
            out[col] = out[col].fillna(fill)
    return out


def normalize_strings(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    for col in out.select_dtypes(include="object").columns:
        out[col] = out[col].astype(str).str.strip()
    return out


def clean(df: pd.DataFrame) -> pd.DataFrame:
    return normalize_strings(
        fill_categorical_missing(
            fill_numeric_missing(drop_duplicates(normalize_column_names(df)))
        )
    )
