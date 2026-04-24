"""Script utilitário para gerar o relatório Markdown."""

from students_habits.cleaner import clean
from students_habits.loader import load_dataset
from students_habits.reports import generate_markdown


def main() -> None:
    df = clean(load_dataset())
    path = generate_markdown(df)
    print(f"Relatório gerado em: {path}")


if __name__ == "__main__":
    main()
