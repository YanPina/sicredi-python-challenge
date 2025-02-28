import heapq
from typing import List

from src.core.logger import logger
from src.models.contract import ContractRequest


class ContractsService:

    @staticmethod
    def get_top_n_open_contracts(request: ContractRequest) -> List[int]:
        """
        Retorna os N maiores devedores que ainda não renegociaram seus débitos.

        Args:
            request (ContractRequest): Objeto contendo os contratos em aberto,
            contratos renegociados e o número máximo de devedores a serem
            retornados.

        Returns:
            List[int]: Lista de IDs dos devedores, ordenada do maior para o
            menor saldo devedor.
        """
        logger.info(
            f"Recebida requisição para obter os {request.top_n} maiores "
            "devedores."
        )
        logger.debug(f"Contratos em aberto: {request.open_contracts}")
        logger.debug(
            f"Contratos renegociados: {request.renegotiated_contracts}"
        )
        renegotiated_set = set(request.renegotiated_contracts)

        filtered_contracts = [
            contract
            for contract in request.open_contracts
            if contract.id not in renegotiated_set
        ]

        logger.debug(f"Contratos após filtragem: {filtered_contracts}")

        top_contracts = heapq.nlargest(
            request.top_n, filtered_contracts, key=lambda c: c.debt
        )

        result = [contract.id for contract in top_contracts]
        logger.info(f"Devedores selecionados: {result}")

        return result


contract_service = ContractsService()
