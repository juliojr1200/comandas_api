from pydantic import BaseModel

class Produto(BaseModel):
    id_produto: int = None
    nome_produto: str
    descricao: str
    foto: bytes = None
    valor_unitario: float