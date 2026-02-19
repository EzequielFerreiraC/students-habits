"""Testes do carregador de dataset."""

import pandas as pd
import pytest

from students_habits.loader import load_dataset, load_sample


def test_load_dataset_returns_dataframe(dataset_path):
    df = load_dataset(dataset_path)
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0
    assert "exam_score" in df.columns


def test_load_sample_limits_rows(dataset_path):
    df = load_sample(n=5, path=dataset_path)
    assert len(df) == 5


def test_load_dataset_missing_path(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_dataset(tmp_path / "missing.csv")
