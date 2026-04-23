# Guia do notebook

O notebook `b_notebooks/habits.ipynb` traz uma exploração interativa do
dataset, estruturado assim:

1. **Setup** — imports e carregamento via `students_habits.loader`.
2. **Cleaning** — aplica `students_habits.cleaner.clean` e mostra o schema
   resultante.
3. **Análise univariada** — distribuições de estudo, sono, redes sociais
   e nota.
4. **Análise bivariada** — scatter e box plots de hábitos vs nota.
5. **Correlações** — heatmap e ranking de correlações com `exam_score`.
6. **Sumário** — chama `analysis.summary.build_summary` para gerar um
   relatório condensado.

Abra com:

```bash
jupyter lab b_notebooks/habits.ipynb
```
