"""Testes do módulo de estatísticas."""

from students_habits.stats import group_means, numeric_summary, top_performers


def test_numeric_summary_columns(sample_df):
    summary = numeric_summary(sample_df)
    assert {"mean", "std", "min", "max"}.issubset(summary.columns)


def test_top_performers_returns_sorted(sample_df):
    top = top_performers(sample_df, n=2)
    assert list(top["exam_score"]) == [95.0, 80.0]


def test_group_means_orders_desc(sample_df):
    means = group_means(sample_df, by="student_id", column="exam_score")
    assert list(means.values) == sorted(means.values, reverse=True)
