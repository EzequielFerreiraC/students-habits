"""Smoke tests para garantir que o pacote importa limpo."""

import importlib

MODULES = [
    "students_habits",
    "students_habits.loader",
    "students_habits.cleaner",
    "students_habits.features",
    "students_habits.stats",
    "students_habits.correlations",
    "students_habits.visualization",
    "students_habits.cli",
]


def test_modules_importable():
    for name in MODULES:
        importlib.import_module(name)
