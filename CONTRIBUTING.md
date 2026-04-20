# Contribuindo

Obrigado por considerar contribuir!

## Fluxo

1. Faça fork do repositório e crie uma branch a partir de `main`.
2. Instale as dependências: `pip install -r requirements.txt`.
3. Rode a suite de testes: `pytest`.
4. Abra um pull request descrevendo a mudança.

## Mensagens de commit

Este projeto segue o padrão `Type: PascalCaseDescription`, por exemplo:

- `Feat: AddSomething`
- `Fix: HandleEdgeCase`
- `Docs: UpdateReadme`
- `Test: AddSomethingTests`
- `Refactor: ExtractSomething`
- `Build: PinDependencies`
- `Chore: AddSomething`

## Pastas

As pastas de topo seguem o padrão `prefix_snake_case` (`a_data`,
`b_notebooks`, `c_src`, `d_tests`, `e_docs`, `z_scripts`) para
forçar uma ordem visual coerente.
