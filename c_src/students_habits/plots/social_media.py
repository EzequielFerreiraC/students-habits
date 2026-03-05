"""Plots focados em uso de redes sociais."""

from __future__ import annotations

import pandas as pd

from ..visualization import plot_scatter


def social_media_vs_score(df: pd.DataFrame):
    return plot_scatter(df, x="social_media_hours", y="exam_score")
