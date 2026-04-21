# Changelog

Todas as mudanças relevantes do projeto.

## [0.2.0] - 2026-04-21

### Adicionado
- Pacote modular em `c_src/students_habits` com loader, cleaner,
  feature engineering, stats, correlations, visualization, plots,
  analysis, model, encoders, reports, export e CLI.
- Suite pytest com testes de loader, cleaner, stats, visualization,
  model, smoke e integração.
- Documentação em `e_docs/` e atalhos de Makefile.
- Estrutura de pastas com prefixos `a_`, `b_`, `c_`, `d_`, `e_`, `z_`.

### Alterado
- Renomeado o módulo `correlation` para `correlations` (alias mantido).
- Helpers de visualização aplicam tight layout e rotacionam labels longos.

### Corrigido
- Tratamento de dataframes vazios nas correlações.
- Tratamento de valores ausentes em colunas categóricas.
- Normalização defensiva de nomes de colunas no cleaner.

## [0.1.0] - 2025-09-23

### Adicionado
- Exploração inicial do dataset em notebook.
