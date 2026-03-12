"""Helpers pequenos compartilhados entre módulos de plot."""

from __future__ import annotations

import matplotlib.pyplot as plt


def new_figure(width: float = 8, height: float = 5):
    return plt.subplots(figsize=(width, height))


def apply_title(ax, title: str) -> None:
    ax.set_title(title)
    ax.title.set_fontsize(13)
