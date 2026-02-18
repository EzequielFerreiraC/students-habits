"""Fixtures compartilhadas do pytest."""

from pathlib import Path

import pandas as pd
import pytest


@pytest.fixture
def dataset_path() -> Path:
    return Path("a_data/student_habits_performance.csv")


@pytest.fixture
def sample_df() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "student_id": ["S1", "S2", "S3"],
            "age": [20, 21, 22],
            "study_hours_per_day": [2.0, 5.5, 7.0],
            "sleep_hours": [7.0, 6.0, 8.0],
            "exam_score": [60.0, 80.0, 95.0],
        }
    )
