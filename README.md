# Students Habits

Análise de dados do dataset `student_habits_performance.csv`, que descreve
hábitos diários de estudantes (estudo, sono, alimentação, redes sociais,
exercício, saúde mental) e a respectiva nota final.

O projeto fornece um pacote Python reutilizável, notebooks de exploração,
uma CLI e scripts utilitários para reproduzir as análises.

## Estrutura

```
a_data/        Dataset bruto
b_notebooks/   Notebooks Jupyter
c_src/         Código fonte do pacote students_habits
d_tests/       Suite pytest
e_docs/        Documentação
z_scripts/     Scripts utilitários
```

## Uso rápido

```bash
pip install -r requirements.txt

# Análise via CLI
python -m students_habits.cli

# Notebook interativo
jupyter lab b_notebooks/habits.ipynb

# Gerar relatório Markdown
python z_scripts/reports/run_report.py
```

## Testes

```bash
pytest
```

## Documentação

Veja a pasta `e_docs/` para guias detalhados de uso, descrição do dataset,
estrutura do projeto e do notebook.

## Autor

Ezequiel Ferreira
