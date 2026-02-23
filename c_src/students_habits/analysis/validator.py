"""Validação de schema do dataset."""

from __future__ import annotations

import pandas as pd

REQUIRED_COLUMNS = {
    "student_id",
    "age",
    "study_hours_per_day",
    "sleep_hours",
    "exam_score",
}


class DatasetValidationError(ValueError):
    """Erro lançado quando o dataset não corresponde ao schema esperado."""


def validate(df: pd.DataFrame) -> None:
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise DatasetValidationError(
            f"Colunas obrigatórias ausentes: {sorted(missing)}"
        )
    if df["exam_score"].min() < 0 or df["exam_score"].max() > 100:
        raise DatasetValidationError("exam_score deve estar entre 0 e 100")
