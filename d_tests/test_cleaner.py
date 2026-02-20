"""Testes do módulo de limpeza."""

import numpy as np
import pandas as pd

from students_habits.cleaner import (
    clean,
    drop_duplicates,
    fill_numeric_missing,
)


def test_drop_duplicates_keeps_first():
    df = pd.DataFrame({"student_id": ["S1", "S1", "S2"], "exam_score": [10, 20, 30]})
    assert len(drop_duplicates(df)) == 2


def test_fill_numeric_missing_fills_median():
    df = pd.DataFrame({"exam_score": [10.0, np.nan, 30.0]})
    filled = fill_numeric_missing(df)
    assert filled["exam_score"].isna().sum() == 0


def test_clean_pipeline(sample_df):
    out = clean(sample_df)
    assert out.isna().sum().sum() == 0
