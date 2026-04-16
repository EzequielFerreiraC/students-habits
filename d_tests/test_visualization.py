"""Testes (nível smoke) dos helpers de visualização."""

import matplotlib

matplotlib.use("Agg")

from students_habits.correlations import correlation_matrix
from students_habits.visualization import (
    plot_correlation_heatmap,
    plot_histogram,
    plot_scatter,
)


def test_plot_histogram_returns_figure(sample_df):
    fig = plot_histogram(sample_df, "exam_score", bins=5)
    assert fig is not None


def test_plot_scatter_returns_figure(sample_df):
    fig = plot_scatter(sample_df, "study_hours_per_day", "exam_score")
    assert fig is not None


def test_plot_correlation_heatmap(sample_df):
    fig = plot_correlation_heatmap(correlation_matrix(sample_df))
    assert fig is not None
