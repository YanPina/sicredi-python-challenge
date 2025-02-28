from src.core.logger import logger
from src.models.contract import Contract, ContractRequest
from src.models.orders import OrderRequest
from src.services.contract_svc import contract_service
from src.services.orders_svc import orders_service


def execute_contract_service() -> None:
    """Executa a lógica do serviço de contratos."""
    contract_request = ContractRequest(
        open_contracts=[
            Contract(id=1, debt=1000.0),
            Contract(id=2, debt=500.0),
            Contract(id=3, debt=1500.0),
            Contract(id=4, debt=2000.0),
            Contract(id=5, debt=2500.0),
        ],
        renegotiated_contracts=[3],
        top_n=3,
    )
    top_debtors = contract_service.get_top_n_open_contracts(contract_request)
    logger.info(f"Top devedores não renegociados: {top_debtors}")


def execute_orders_service() -> None:
    """Executa a lógica do serviço de ordens."""
    order_request = OrderRequest(requests=[70, 50, 80, 50], n_max=100)
    min_trips = orders_service.combine_orders(order_request)
    logger.info(f"Número mínimo de viagens necessárias: {min_trips}")


def main() -> None:
    execute_contract_service()
    execute_orders_service()


if __name__ == "__main__":
    main()
