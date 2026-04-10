"""Gerador de relatório em Markdown."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from .analysis.summary import build_summary
from .paths import OUTPUT_DIR


def generate_markdown(df: pd.DataFrame, name: str = "report") -> Path:
    summary = build_summary(df)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUTPUT_DIR / f"{name}.md"

    parts = ["# Relatório Students Habits\n"]
    parts.append("## Resumo numérico\n")
    parts.append(summary["describe"].round(2).to_markdown())
    parts.append("\n\n## Top correlações com exam_score\n")
    parts.append(summary["top_correlations"].round(3).to_markdown())
    parts.append("\n\n## Nota média por qualidade da alimentação\n")
    parts.append(summary["score_by_diet"].round(2).to_markdown())

    out.write_text("\n".join(parts))
    return out
