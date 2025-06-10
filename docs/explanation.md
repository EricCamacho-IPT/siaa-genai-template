# Explicação e Decisões de Design

Nesta seção, explicamos o "porquê" por trás de algumas das escolhas tecnológicas e de design deste template.

### Por que `uv` em vez de `poetry` ou `pip`?

-   **Velocidade:** `uv` é uma ferramenta da nova geração, escrita em Rust, com velocidades maiores que usando `pip` ou `poetry` para resolver e instalar dependências. Em projetos de IA com muitas bibliotecas pesadas, isso faz uma grande diferença.
-   **Simplicidade:** Ele adota o formato padrão `requirements.txt`, que é universalmente entendido, ao mesmo tempo que oferece um resolvedor de dependências moderno e cache global.

### Por que FastAPI?

-   **Performance:** É um dos frameworks web Python mais rápidos disponíveis, ideal para servir modelos que precisam de baixa latência.
-   **Tipagem Moderna:** Usa type hints do Python para validação de dados com Pydantic, o que torna as APIs mais robustas e menos propensas a erros.
-   **Auto-documentação:** Gera automaticamente uma documentação interativa da API (com Swagger UI), o que é extremamente útil para os consumidores da sua API.

### Por que uma Estrutura de Pastas Detalhada?

A estrutura com `data/`, `src/`, `notebooks/`, etc., é baseada em padrões bem estabelecidos na comunidade de Ciência de Dados (como o [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/)). Ela promove:

-   **Reprodutibilidade:** Separar dados, código e notebooks torna mais fácil para outros (e para você no futuro) entenderem e reproduzirem seu trabalho.
-   **Manutenibilidade:** Código modular em `src/` é mais fácil de testar e manter do que scripts soltos.
