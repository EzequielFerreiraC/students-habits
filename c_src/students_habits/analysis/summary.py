"""Relatório resumo de alto nível para o dataset."""

from __future__ import annotations

import pandas as pd

from ..correlations import correlations_with
from ..stats import group_means, numeric_summary


def build_summary(df: pd.DataFrame) -> dict[str, pd.DataFrame | pd.Series]:
    return {
        "describe": numeric_summary(df),
        "score_by_gender": group_means(df, by="gender", column="exam_score"),
        "score_by_diet": group_means(df, by="diet_quality", column="exam_score"),
        "top_correlations": correlations_with(df, "exam_score").head(5),
    }
