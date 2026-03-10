"""Plots focados em saúde mental."""

from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def mental_health_vs_score(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.lineplot(
        data=df.groupby("mental_health_rating")["exam_score"].mean().reset_index(),
        x="mental_health_rating",
        y="exam_score",
        marker="o",
        ax=ax,
    )
    ax.set_title("Nota média por rating de saúde mental")
    return fig
