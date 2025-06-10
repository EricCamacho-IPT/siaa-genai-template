# Agentes

Ao escolher um `llm_framework` (`crewai`, `langgraph` ou `pydanticai`), o template cria uma estrutura de pastas em `agents` para orquestrar sistemas multi-agente.

-   **`crew.py`**: Onde você define seus agentes. Cada agente terá um papel (role), um objetivo (goal) e ferramentas (tools) específicas.

-   **`tasks.py`**: Aqui você define as tarefas que serão atribuídas aos agentes. Cada tarefa é uma unidade de trabalho que contribui para o objetivo final da equipe.


Esta separação ajuda a gerenciar a complexidade de múltiplos agentes trabalhando juntos.