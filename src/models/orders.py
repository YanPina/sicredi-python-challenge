from typing import List

from pydantic import BaseModel, Field


class OrderRequest(BaseModel):  # type: ignore
    requests: List[int] = Field(
        ...,
        description="Lista de valores monetários requisitados por agências "
        "para transporte de dinheiro.",
    )
    n_max: int = Field(
        ...,
        description="Valor máximo permitido por viagem de transporte de "
        "dinheiro, respeitando o limite de dois pedidos por viagem.",
    )
