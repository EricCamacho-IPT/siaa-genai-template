# SIAA GenAI Template

[![Status](https://img.shields.io/badge/status-ativo-success.svg)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

Um template para criar projetos para LLMs de forma rápida e padronizada.

Este template gera um esqueleto de projeto completo com `FastAPI`, `uv` (gerenciamento de dependências), `Docker` e um workflow de CI/CD com `GitHub Actions`.

## ✨ Documentação do Template

[SIAA GenAI](https://ipt.github.io/siaa-genai-template/)

## ✨ Funcionalidades Principais

-   **Estrutura de Projeto Profissional**: Gera uma estrutura de pastas organizada para `dados`, `configurações`, `notebooks` e `documentação`.
-   **Modularidade**: O template permite a instalação opcional de pacotes para diferentes casos de uso, como RAG e frameworks específicos (LangChain, LangGraph, CrewAI, PydanticAI, Transformers).
-   **Geração Condicional**: Cria automaticamente pastas e códigos para **RAG** ou **frameworks de Agentes** (CrewAI, LangGraph ou PydanticAI) apenas se você escolher essas opções.
-   **Gerenciamento de Configuração com Hydra**: Integração opcional com `Hydra` para um gerenciamento de configurações limpo e poderoso.
-   **Documentação com MkDocs**: Opção para gerar um site de documentação pronto para uso com `MkDocs`.
-   **API com FastAPI**: Estrutura de API pronta para servir modelos, com endpoints para geração de texto e health check.
-   **Gerenciamento de Dependências com uv**: Utiliza `uv` para uma instalação e gerenciamento de pacotes.
-   **Setup Automatizado**: Um hook pós-geração pergunta ao usuário se deseja criar o ambiente virtual e instalar todas as dependências automaticamente.
-   **Containerização com Docker**: `Dockerfile` otimizado e multi-estágio para criar imagens leves e seguras para produção.
-   **Automação com Makefile**: Comandos prontos para instalar, testar, rodar a aplicação e gerenciar a imagem Docker.
-   **Qualidade de Código**: Configurado com `ruff` para linting e formatação, garantindo um código limpo e consistente.
-   **Integração Contínua**: Workflow de GitHub Actions que roda testes e lint a cada push ou pull request.

## 🚀 Como Usar!!

Para gerar um novo projeto usando este template, certifique-se de que você tem o [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html) instalado:

```bash
pip install cookiecutter
```
Em seguida, rode o seguinte comando e responda às perguntas:
```bash
cookiecutter gh:ipt/siaa-genai-template
```

### ⚙️ Opções do Template

O Cookiecutter irá solicitar que você preencha os seguintes valores:

| Variável            | Descrição                                                                               | Valor Padrão                                            |
| --------------------| --------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| `project_name`      | O nome do seu projeto (ex: "Meu Chatbot Inteligente")                                   | `LLM Project`                                           |
| `project_slug`      | A versão do nome para uso em URLs e nomes de pasta                                      | `llm-project`                                           |
| `package_name`      | O nome do pacote Python que será gerado                                                 | `llm_project`                                           |
| `author_name`       | Seu nome                                                                                | `Seu Nome`                                              |
| `author_email`      | Seu e-mail                                                                              | `[seu_email@exemplo.com](mailto:your.email@example.com)`|
| `description`       | Uma breve descrição do projeto                                                          | `Uma breve descrição do projeto`                        |
| `license`           | A licença do software para o projeto gerado                                             | `MIT`                                                   |
| `llm_framework`     | Framework principal para LLM (langchain, transformers, etc.)                            | `langchain`                                             |
| `agent_framework`   | Framework de agentes a ser utilizado (langgraph, crewai, pydanticai)                    | `none`                                                  |
| `use_rag`           | (y/n) Gerar estrutura de pastas e arquivos para RAG?                                    | `n`                                                     |
| `use_mkdocs`        | (y/n) Gerar estrutura de documentação com MkDocs?                                       | `y`                                                     |
| `use_hydra`         | (y/n) Gerar estrutura de configuração com Hydra?                                        | `y`                                                     |
| `run_initial_setup` | Pergunta se o ambiente virtual deve ser criado e dependências instaladas após a geração | `y`                                                     |

### 🛠️ Estrutura Condicional do Projeto Gerado

A estrutura final do seu projeto dependerá das suas respostas.

- Se `use_rag == 'y'`, uma pasta `src/{{cookiecutter.package_name}}/rag/` será criada com scripts para embeddings, vector store e retrievers.
- Se `agent_framework` for `crewai`, `langgraph` ou `pydanticai`, uma pasta `src/{{cookiecutter.package_name}}/agents/` será criada com uma estrutura modular para agentes e tarefas.
- Se `use_mkdocs == 'y'`, uma pasta `docs/` e um arquivo `mkdocs.yml` serão adicionados ao seu projeto.
- Se `use_hydra == 'y'`, uma pasta `config/` será criada

### 🛠️ Após a Geração do Projeto

Se você respondeu `'y'` para `run_initial_setup`, o template irá automaticamente:

1. Criar um ambiente virtual (`.venv`).
2. Instalar `uv` dentro deste ambiente.
3. Instalar todas as dependências de desenvolvimento listadas em `requirements-dev.txt`.

Se você respondeu `'n'` para ara `run_initial_setup`, você receberá instruções para ativar seu novo ambiente virtual:

Em Linux/macOS
```bash
source .venv/bin/activate
```

Em Windows
```bash
.venv\Scripts\activate
```
E seu projeto estará pronto para rodar!

### 🤝 Como Contribuir para este Template
Contribuições para melhorar este template são muito bem-vindas! Sinta-se à vontade para:
- Abrir uma issue para reportar um bug ou sugerir uma melhoria.
- Enviar um Pull Request com suas alterações.

### 📄 Licença do Template
Este template Cookiecutter está licenciado sob a Licença MIT. Os projetos gerados por ele podem usar a licença que você escolher durante a configuração.
