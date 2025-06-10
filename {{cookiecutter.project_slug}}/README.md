# {{ cookiecutter.project_name }}

[![License](https://img.shields.io/badge/license-{{ cookiecutter.license }}-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-{{ cookiecutter.python_version }}-blue.svg)](https://www.python.org/)
[![Build Status](https://github.com/seu-usuario/{{ cookiecutter.project_slug }}/actions/workflows/ci.yml/badge.svg)](https://github.com/seu-usuario/{{ cookiecutter.project_slug }}/actions)

> {{ cookiecutter.description }}

---

## 🚀 Visão Geral

Este repositório contém o código-fonte e a estrutura para o projeto **{{ cookiecutter.project_name }}**. 

Ele foi gerado usando um template Cookiecutter especializado para aplicações de Modelos de Linguagem (LLM), fornecendo uma base sólida para desenvolvimento, testes e implantação.

## ✨ Funcionalidades

* **Estrutura de Projeto Profissional**: Organização de pastas para dados, notebooks, configurações e código-fonte, facilitando a manutenção e escalabilidade.
* **Geração Condicional**: Estruturas de código para **RAG** e **Agentes** são criadas automaticamente com base nas suas escolhas, mantendo o projeto limpo.
* **API com FastAPI**: Ponto de entrada de API pronto para servir o modelo, com endpoints para inferência e health check.
* **Gerenciamento de Dependências com uv**: Utiliza `uv` para uma instalação e gerenciamento de pacotes extremamente rápidos.
* **Setup Automatizado**: Um script interativo configura o ambiente virtual e instala as dependências iniciais para você.
* **Containerização com Docker**: `Dockerfile` otimizado para criar imagens leves e seguras.
{%- if cookiecutter.use_mkdocs == 'y' %}
* **Documentação com MkDocs**: Um site de documentação pronto para ser preenchido e publicado.
{%- endif %}
{%- if cookiecutter.use_hydra == 'y' %}
* **Configuração com Hydra**: Gerenciamento de configurações centralizado e flexível.
{%- endif %}
* **Automação com `Makefile`**: Comandos para instalar, testar, rodar a aplicação e gerenciar a imagem Docker.
* **CI/CD com GitHub Actions**: Workflow pronto para validar a qualidade do código a cada push/pull request.

## 🏁 Como Começar

Siga os passos abaixo para configurar e rodar o projeto localmente.

### Pré-requisitos

* Python {{ cookiecutter.python_version }}
* Git

### Instalação

Ao gerar o projeto com o Cookiecutter, você será perguntado se deseja executar a configuração inicial. Se respondeu 'y', os seguintes passos foram executados automaticamente:

1.  Criação de um ambiente virtual em `.venv`.
2.  Instalação de todas as dependências de desenvolvimento usando `uv`.

Se você optou por não fazer a configuração automática, siga os passos manuais:


1.  **Crie e ative o ambiente virtual (Recomendado):**
Use o Makefile para simplificar:

```bash
make setup
source .venv/bin/activate
```

No Windows: 
```bash
.venv\Scripts\activate
```

Ou manualmente:
```bash
python -m venv .venv
source .venv/bin/activate
```

3.  **Instale as dependências com uv:**
O Makefile também pode fazer isso por você:

```bash
make install
```
Ou manualmente com `uv` (após ativar o ambiente virtual):

```bash
uv pip install -r requirements-dev.txt
```

### Rodando o Servidor de Desenvolvimento

Para iniciar o servidor FastAPI com recarregamento automático (hot-reload), use o Makefile:
```bash
make run
```

Ou manualmente com uv (com o ambiente virtual ativo):
```bash
uv run uvicorn {{ cookiecutter.package_name }}.app:app --host 0.0.0.0 --port 8000 --reload
```

A API estará disponível em http://localhost:8000.

### Instalações Opcionais

Este template vem com comandos para instalar conjuntos de dependências para funcionalidades específicas. Use-os conforme a necessidade:

- Para RAG (Retrieval-Augmented Generation):

```bash
make install-rag
```

- Para usar o framework LangChain:

```bash
make install-langchain
```

- Para usar a biblioteca Transformers:

```bash
make install-transformers
```

### 🐳 Uso com Docker

1. Construa a imagem Docker:

```bash
make docker-build
```

2. Rode o container:

```bash
docker run -p 8000:8000 {{ cookiecutter.docker_image_name }}:latest
```

### 🧪 Testes

Para rodar a suíte de testes automatizados:
```bash
make test
```

### 📂 Estrutura do Projeto.
```bash
.
├── .env                    # Variáveis de ambiente
├── .github/workflows/      # Workflows de CI/CD (GitHub Actions)
{%- if cookiecutter.use_hydra == 'y' %}
├── config/                 # Arquivos de configuração (gerenciado pelo Hydra)
{%- endif %}
├── data/
│   ├── external/           # Dados de fontes externas
│   ├── features/           # Dados sobre as variáveis/metadados
│   ├── intermediate/       # Dados intermediários, após transformações
│   ├── processed/          # Dados finais, prontos para modelagem
│   └── raw/                # Dados originais e imutáveis
{%- if cookiecutter.use_mkdocs == 'y' %}
├── docs/                   # Arquivos da documentação gerada com MkDocs
{%- endif %}
├── notebooks/              # Jupyter Notebooks para exploração e experimentação
├── src/
│   └── {{ cookiecutter.package_name }}/  # Código-fonte principal do projeto
│       {%- if cookiecutter.llm_framework != 'none' %}
│       ├── agents/         # Lógica para Agentes (tasks, crew, etc.)
│       {%- endif %}
│       {%- if cookiecutter.use_rag == 'y' %}
│       ├── rag/            # Lógica para RAG (embeddings, vector store, etc.)
│       {%- endif %}
│       ├── __init__.py
│       ├── app.py          # Lógica da API (FastAPI)
│       ├── llm.py          # Lógica de carregamento e inferência do LLM
│       ├── schemas.py      # Schemas Pydantic para as requisições/respostas
│       └── utils.py        # Funções uteis para o projeto
├── tests/                  # Testes automatizados
├── .gitignore              # Arquivos e pastas a serem ignorados pelo Git
├── Dockerfile              # Instruções para construir a imagem Docker
├── LICENSE                 # Licença do projeto
├── Makefile                # Comandos para automação de tarefas
{%- if cookiecutter.use_mkdocs == 'y' %}
├── mkdocs.yml              # Configuração do site de documentação
{%- endif %}
├── pyproject.toml          # Configuração do projeto (metadados, ruff, etc.)
├── requirements.txt        # Dependências de produção
├── requirements-dev.txt    # Dependências de desenvolvimento
└── README.md               # Este arquivo
```

### Endpoints da API
- <code>POST /generate</code>: Envie um prompt para o modelo e receba a resposta gerada.
    - Corpo da Requisição: <code>{"prompt": "seu texto aqui"}</code>
    - Resposta: <code>{"response": "texto gerado pelo modelo"}</code>
    
- <code>GET /health</code>: Verifica o status da aplicação.
    - Resposta: <code>{"status": "ok"}</code>
    
### 🤝 Contribuindo
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou um pull request.

### 📄 LicençaEste projeto está licenciado sob a Licença {{ cookiecutter.license }}. 
Veja o arquivo LICENSE para mais detalhes.
