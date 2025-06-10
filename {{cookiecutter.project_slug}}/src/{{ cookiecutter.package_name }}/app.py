# Para que serve este arquivo:
# Este é o ponto de entrada da sua API. Ele usa o framework FastAPI para criar
# os endpoints. A lógica principal é simples: receber requisições HTTP,
# passar os dados para a camada de lógica do modelo (llm.py) e retornar a resposta.

# Como modificar conforme seu projeto:
# - Adicione novos endpoints para diferentes funcionalidades (ex: um endpoint para
#   RAG, outro para classificação de texto).
# - Melhore o tratamento de erros e o logging para produção.
# - Integre um sistema de autenticação se a API não for pública.

from fastapi import FastAPI
from .schemas import GenerateRequest, GenerateResponse, HealthResponse
from .llm import get_llm_response

# Cria a instância da aplicação FastAPI
app = FastAPI(
    title="{{ cookiecutter.project_name }}",
    description="{{ cookiecutter.description }}",
    version="{{ cookiecutter.version }}",
)

@app.post("/generate", response_model=GenerateResponse)
async def generate(request: GenerateRequest):
    """
    Recebe um prompt e retorna a resposta gerada pelo LLM.
    """
    response_text = await get_llm_response(request.prompt)
    return GenerateResponse(response=response_text)

@app.get("/health", response_model=HealthResponse)
async def health():
    """
    Endpoint de health check para verificar se a aplicação está no ar.
    """
    return HealthResponse(status="ok")

# Para que o uvicorn encontre o app, o nome do arquivo deve ser `app.py`
# e a instância do FastAPI deve se chamar `app`.
