.PHONY: install test run report clean

install:
	pip install -r requirements.txt

test:
	pytest

run:
	python -m students_habits.cli

report:
	python z_scripts/run_report.py

clean:
	rm -rf .pytest_cache **/__pycache__ z_output
