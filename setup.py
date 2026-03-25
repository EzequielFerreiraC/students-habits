from setuptools import find_packages, setup

setup(
    name="students-habits",
    version="0.2.0",
    description="Análise de hábitos de estudantes e desempenho em exames.",
    author="Ezequiel Ferreira",
    package_dir={"": "c_src"},
    packages=find_packages(where="c_src"),
    python_requires=">=3.10",
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
    ],
    entry_points={
        "console_scripts": [
            "students-habits=students_habits.cli:main",
        ],
    },
)
