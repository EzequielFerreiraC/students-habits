"""Entrypoint de linha de comando para análises rápidas."""

from __future__ import annotations

import argparse

from .analysis.categorizer import add_performance_label
from .analysis.summary import build_summary
from .cleaner import clean
from .loader import load_dataset


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Students habits analysis CLI")
    parser.add_argument("--path", default=None, help="Caminho para o CSV")
    parser.add_argument("--top-n", type=int, default=5)
    args = parser.parse_args(argv)

    df = add_performance_label(clean(load_dataset(args.path)))
    summary = build_summary(df)

    print("=== Resumo numérico ===")
    print(summary["describe"].round(2))
    print("\n=== Top correlações com exam_score ===")
    print(summary["top_correlations"].round(3))
    print("\n=== Nota por qualidade da alimentação ===")
    print(summary["score_by_diet"].round(2))
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
