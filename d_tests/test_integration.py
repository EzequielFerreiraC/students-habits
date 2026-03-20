"""Smoke test ponta-a-ponta do pipeline de análise."""

from students_habits.analysis.categorizer import add_performance_label
from students_habits.analysis.summary import build_summary
from students_habits.cleaner import clean
from students_habits.loader import load_dataset


def test_full_pipeline_runs(dataset_path):
    df = load_dataset(dataset_path)
    df = clean(df)
    df = add_performance_label(df)
    summary = build_summary(df)
    assert "describe" in summary
    assert df["performance"].notna().any()
