# Guia de Início Rápido

Siga estes passos para gerar seu primeiro projeto com o **SIAA GenAI Template**.

### 1. Pré-requisitos

Antes de começar, garanta que você tenha o `cookiecutter` instalado globalmente em seu sistema:

```bash
pip install cookiecutter
```

### 2. Gerando o Projeto

Execute o seguinte comando no seu terminal. Ele clonará o template e iniciará o processo de configuração interativo.

```bash
cookiecutter gh:EricCamacho-IPT/siaa-genai-template
```

Você será guiado por uma série de perguntas para configurar seu projeto, como nome, autor e quais funcionalidades deseja incluir.

### 3. Configuração Inicial Automatizada

Após a geração dos arquivos, o template irá perguntar se você deseja que ele configure o ambiente virtual e instale as dependências automaticamente.

`Deseja configurar o ambiente e instalar as dependências agora? [y/n]: y`

Se você responder `sim` (o padrão), o template irá:

1. Criar um ambiente virtual (`.venv`).
2. Instalar `uv` dentro deste ambiente.
3. Instalar todas as dependências listadas em `requirements-dev.txt`

### 4. Ativando o Ambiente

Entre na pasta do seu novo projeto e ative o ambiente virtual recém-criado:

`cd <nome_do_seu_projeto>`

No Linux/macOS

```bash
source .venv/bin/activate`
```

No Windows

```bash
.venv\Scripts\activate
```