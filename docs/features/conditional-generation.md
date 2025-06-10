# Geração Condicional de Código

A principal vantagem deste template é sua capacidade de gerar uma estrutura de projeto enxuta, contendo apenas o que você precisa. Isso é feito através da **geração condicional** de arquivos e pastas.

Durante a configuração, você responderá a perguntas como `use_rag` e `llm_framework`. Com base nas suas respostas, o Cookiecutter irá:

-   **Criar a pasta `src/package_name/rag/`** apenas se `use_rag` for 'y'.
-   **Criar a pasta `src/package_name/agents/`** apenas se um `llm_framework` for selecionado (`crewai`, `langgraph`, `pydanticai`).
-   **Adicionar o arquivo `mkdocs.yml` e a pasta `docs/`** apenas se `use_mkdocs` for 'y'.
-   **Criar a pasta `config/`** apenas se `use_hydra` for 'y'.

Isso mantém o projeto gerado limpo, sem códigos ou configurações desnecessárias.
