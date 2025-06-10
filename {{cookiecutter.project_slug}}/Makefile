# Para que serve este arquivo:
# Um Makefile automatiza tarefas comuns de desenvolvimento. Em vez de lembrar e digitar
# comandos longos, você pode simplesmente rodar `make <target>`. Este Makefile
# oferece targets para instalação, lint, testes, execução do servidor e operações com Docker.

# Como modificar conforme seu projeto:
# - Adicione novos targets para tarefas repetitivas do seu projeto (ex: `make data-download`).
# - Modifique os targets existentes se precisar de flags ou comportamentos diferentes.

.PHONY: help setup install lint test run clean docker-build docker-push

# Definição de variáveis
PYTHON = python
VENV_DIR = .venv
DOCKER_IMAGE_NAME = {{ cookiecutter.docker_image_name }}
DOCKER_TAG ?= latest

# Garante que os comandos sejam executados com o `uv` do ambiente virtual, se ele existir
UV := $(VENV_DIR)/bin/uv
ifeq ($(wildcard $(UV)),)
	UV := uv
endif

help:
	@echo "Opções disponíveis:"
	@echo "  setup          Cria um ambiente virtual Python com o venv."
	@echo "  install        Instala todas as dependências de desenvolvimento e produção com uv."
	@echo "  lint           Roda o linter (ruff) para verificar o estilo do código."
	@echo "  test           Roda os testes automatizados com pytest."
	@echo "  run            Inicia o servidor de desenvolvimento com hot-reload."
	@echo "  clean          Remove arquivos de cache e build."
	@echo "  docker-build   Constrói a imagem Docker para o projeto."
	@echo "  docker-push    Envia a imagem Docker para um registro (configure o nome da imagem)."

setup:
	@echo ">>> Configurando ambiente virtual em $(VENV_DIR)..."
	$(PYTHON) -m venv $(VENV_DIR)
	@echo "Ambiente criado."
	@echo "Para ativar, rode: source $(VENV_DIR)/bin/activate"

install: setup
	@echo ">>> Instalando dependências com uv..."
	$(UV) pip install -r requirements-dev.txt

lint:
	@echo ">>> Verificando o estilo do código com ruff..."
	$(UV) run ruff check .

test:
	@echo ">>> Rodando testes com pytest..."
	$(UV) run pytest

run:
	@echo ">>> Iniciando o servidor de desenvolvimento em http://localhost:8000"
	$(UV) run uvicorn {{ cookiecutter.package_name }}.app:app --host 0.0.0.0 --port 8000 --reload

clean:
	@echo ">>> Limpando arquivos de build e cache..."
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .pytest_cache
	rm -rf .ruff_cache

docker-build:
	@echo ">>> Construindo imagem Docker: $(DOCKER_IMAGE_NAME):$(DOCKER_TAG)"
	docker build -t $(DOCKER_IMAGE_NAME):$(DOCKER_TAG) .

docker-push:
	@echo ">>> Enviando imagem Docker para o registro..."
	# Certifique-se de estar logado no seu registro Docker (ex: docker login)
	docker push $(DOCKER_IMAGE_NAME):$(DOCKER_TAG)
