"""Plots focados em sono vs desempenho."""

from __future__ import annotations

import pandas as pd

from ..visualization import plot_histogram, plot_scatter


def sleep_distribution(df: pd.DataFrame):
    return plot_histogram(df, column="sleep_hours")


def sleep_vs_score(df: pd.DataFrame):
    return plot_scatter(df, x="sleep_hours", y="exam_score")
