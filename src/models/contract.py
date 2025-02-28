from typing import List

from pydantic import BaseModel, Field


class Contract(BaseModel):  # type: ignore
    id: int = Field(..., description="ID único do correntista")
    debt: float = Field(
        ..., description="Total da dívida acumulada pelo correntista"
    )


class ContractRequest(BaseModel):  # type: ignore
    open_contracts: List[Contract] = Field(
        ...,
        description="Lista de contratos financeiros em aberto, representando"
        "devedores e seus respectivos valores de dívida.",
    )
    renegotiated_contracts: List[int] = Field(
        ...,
        description="Lista de IDs dos correntistas que já renegociaram "
        "seus débitos.",
    )
    top_n: int = Field(
        ...,
        description="Número máximo de devedores a serem retornados, ordenados "
        "do maior para o menor saldo devedor.",
    )
