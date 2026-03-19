"""Caminhos centralizados do projeto."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "a_data"
DEFAULT_DATASET = DATA_DIR / "student_habits_performance.csv"
OUTPUT_DIR = ROOT / "z_output"
