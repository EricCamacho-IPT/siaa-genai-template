# Estrutura Principal do Projeto

Todo projeto gerado com este template compartilha uma estrutura de pastas principal, projetada para organização e escalabilidade.

-   **`config/`**: (Opcional, se `use_hydra='y'`) Contém os arquivos de configuração `.yaml` gerenciados pelo Hydra. Permite separar a lógica das configurações de parâmetros.

-   **`data/`**: Destinada a todos os dados do projeto. É subdividida para refletir o ciclo de vida dos dados:
    -   `external/`: Dados de fontes de terceiros.
    -   `features/`: Dados sobre as variáveis/metadados.
    -   `raw/`: Dados originais e imutáveis.
    -   `intermediate/`: Dados intermediários, após alguma limpeza ou transformação.
    -   `processed/`: Dados finais, limpos e prontos para serem usados por modelos.

-   **`docs/`**: (Opcional, se `use_mkdocs='y'`) Contém os arquivos para a documentação do projeto específico (não do template).

-   **`notebooks/`**: Jupyter Notebooks para análise exploratória de dados, prototipagem e experimentação.

-   **`src/nome_do_seu_pacote`**: O coração da sua aplicação. Todo o código-fonte Python fica aqui.

-   **`tests/`**: Testes automatizados (unitários, de integração, etc.).