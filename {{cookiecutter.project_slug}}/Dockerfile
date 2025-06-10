# Para que serve este arquivo:
# O Dockerfile contém as instruções para construir uma imagem Docker do seu projeto.
# Isso garante que sua aplicação rode da mesma forma em qualquer ambiente (desenvolvimento,
# staging, produção), encapsulando o código e suas dependências.

# Como modificar conforme seu projeto:
# - Altere a imagem base do Python (FROM) se precisar de uma versão diferente.
# - Adicione comandos `RUN` para instalar dependências do sistema operacional (ex: `apt-get install`).
# - Se seu projeto precisar de arquivos adicionais, adicione novos comandos `COPY`.

# Estágio 1: Build - Instalação de dependências
FROM python:{{ cookiecutter.python_version }}-slim as builder

# Define o diretório de trabalho
WORKDIR /app

# Previne que o Python gere arquivos .pyc
ENV PYTHONDONTWRITEBYTECODE 1
# Garante que a saída do Python não seja bufferizada
ENV PYTHONUNBUFFERED 1

# Instala o uv
RUN pip install uv

# Copia o arquivo de dependências de produção
COPY requirements.txt .

# Instala as dependências de produção usando o cache do uv no ambiente do sistema
RUN uv pip install --system --no-cache -r requirements.txt

# Estágio 2: Final - Imagem de produção enxuta
FROM python:{{ cookiecutter.python_version }}-slim

WORKDIR /app

# Copia o ambiente python com as dependências instaladas do estágio de build
COPY --from=builder /usr/local/lib/python{{ cookiecutter.python_version }}/site-packages/ /usr/local/lib/python{{ cookiecutter.python_version }}/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# Copia o código-fonte da aplicação
COPY src/{{ cookiecutter.package_name }}/ /app/{{ cookiecutter.package_name }}/

# Expõe a porta que a aplicação irá rodar
EXPOSE 8000

# Comando para iniciar a aplicação quando o container for executado
CMD ["uvicorn", "{{ cookiecutter.package_name }}.app:app", "--host", "0.0.0.0", "--port", "8000"]
