# Configuração com Hydra

Se `use_hydra: 'y'` for selecionado, seu projeto virá configurado para usar o [Hydra](https://hydra.cc/), uma poderosa biblioteca para gerenciamento de configurações.

Uma pasta `config/` será criada na raiz do projeto, contendo `config.yaml`.

**Vantagens:**

-   **Separação**: Mantém suas configurações (parâmetros de modelo, caminhos de arquivo, etc.) fora do seu código Python.
-   **Flexibilidade na Linha de Comando**: Você pode facilmente sobrescrever qualquer configuração via linha de comando. Ex: `python seu_script.py model.temperature=0.9`.
-   **Composição**: Permite criar configurações complexas combinando múltiplos arquivos `.yaml`.

O Hydra é ideal para experimentação, permitindo que você teste diferentes hiperparâmetros sem alterar o código.