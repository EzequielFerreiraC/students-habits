"""Script utilitário para exportar uma versão limpa do dataset."""

from students_habits.cleaner import clean
from students_habits.export import export_dataframe
from students_habits.loader import load_dataset


def main() -> None:
    df = clean(load_dataset())
    path = export_dataframe(df, name="student_habits_clean")
    print(f"Dataset limpo salvo em: {path}")


if __name__ == "__main__":
    main()
