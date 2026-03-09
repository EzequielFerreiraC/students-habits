"""Plots focados em frequência de exercício."""

from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def exercise_vs_score(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(data=df, x="exercise_frequency", y="exam_score", ax=ax)
    ax.set_title("Nota média por frequência de exercício")
    return fig
