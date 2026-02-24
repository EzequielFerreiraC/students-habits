"""Helpers de engenharia de atributos."""

from __future__ import annotations

import pandas as pd

SCREEN_COLUMNS = ("social_media_hours", "netflix_hours")


def add_screen_time(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["screen_time_hours"] = sum(out[c] for c in SCREEN_COLUMNS if c in out)
    return out


def add_study_to_screen_ratio(df: pd.DataFrame) -> pd.DataFrame:
    out = add_screen_time(df)
    out["study_screen_ratio"] = out["study_hours_per_day"] / out[
        "screen_time_hours"
    ].replace(0, 1)
    return out


def add_sleep_deficit(df: pd.DataFrame, target: float = 8.0) -> pd.DataFrame:
    out = df.copy()
    out["sleep_deficit"] = (target - out["sleep_hours"]).clip(lower=0)
    return out
