# Para que serve este arquivo:
# Este arquivo define os "shapes" dos dados que sua API espera receber (Requests)
# e que ela irá enviar (Responses). Usamos Pydantic para criar esses modelos,
# o que garante validação automática dos dados e uma ótima documentação da API.

# Como modificar conforme seu projeto:
# - Adicione novos campos aos seus schemas se precisar de mais dados
#   (ex: `temperature`, `max_tokens` para o GenerateRequest).
# - Crie novos schemas para novos endpoints.

from pydantic import BaseModel

class GenerateRequest(BaseModel):
    """
    Schema para a requisição do endpoint /generate.
    """
    prompt: str

class GenerateResponse(BaseModel):
    """
    Schema para a resposta do endpoint /generate.
    """
    response: str

class HealthResponse(BaseModel):
    """
    Schema para a resposta do endpoint /health.
    """
    status: str
