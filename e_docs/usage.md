# Uso

## CLI

```bash
python -m students_habits.cli --path a_data/student_habits_performance.csv
```

## Biblioteca

```python
from students_habits.loader import load_dataset
from students_habits.cleaner import clean
from students_habits.analysis.summary import build_summary

df = clean(load_dataset())
report = build_summary(df)
print(report["top_correlations"])
```
