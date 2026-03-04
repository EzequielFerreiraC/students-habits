"""Plots focados em tempo de estudo vs desempenho."""

from __future__ import annotations

import pandas as pd

from ..visualization import plot_scatter


def study_vs_score(df: pd.DataFrame):
    return plot_scatter(df, x="study_hours_per_day", y="exam_score")
