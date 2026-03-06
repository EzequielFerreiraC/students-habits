"""Plots focados em qualidade da alimentação."""

from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def diet_vs_score(df: pd.DataFrame):
    order = ["Poor", "Fair", "Good"]
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(data=df, x="diet_quality", y="exam_score", order=order, ax=ax)
    ax.set_title("Nota por qualidade da alimentação")
    return fig
