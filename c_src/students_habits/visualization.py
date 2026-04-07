"""Helpers de plotagem reutilizáveis (matplotlib + seaborn)."""

from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style="whitegrid")


def _tight(fig):
    fig.tight_layout()
    return fig


def plot_histogram(df: pd.DataFrame, column: str, bins: int = 20):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(df[column].dropna(), bins=bins, kde=True, ax=ax)
    ax.set_title(f"Distribuição de {column}")
    return _tight(fig)


def plot_scatter(df: pd.DataFrame, x: str, y: str, hue: str | None = None):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(data=df, x=x, y=y, hue=hue, ax=ax)
    ax.set_title(f"{y} vs {x}")
    for label in ax.get_xticklabels():
        label.set_rotation(30)
        label.set_ha("right")
    return _tight(fig)


def plot_correlation_heatmap(corr: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    ax.set_title("Mapa de correlações")
    for label in ax.get_xticklabels():
        label.set_rotation(45)
        label.set_ha("right")
    return _tight(fig)
