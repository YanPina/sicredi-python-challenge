from src.core.logger import logger
from src.models.orders import OrderRequest


class OrdersService:

    @staticmethod
    def combine_orders(request: OrderRequest) -> int:
        """
        Calcula o número mínimo de viagens necessárias para atender todas as
        requisições.

        Args:
            request (OrderRequest): Objeto contendo a lista de valores
            monetários requisitados e o valor máximo permitido por viagem.

        Returns:
            int: Número mínimo de viagens.
        """
        logger.info(
            "Recebida requisição para otimizar entregas de valores: "
            f"{request.requests}"
        )
        requests = request.requests.copy()
        requests.sort()
        logger.debug(f"Requisições ordenadas: {requests}")
        left, right = 0, len(requests) - 1
        trips = 0

        while left <= right:
            if requests[left] + requests[right] <= request.n_max:
                logger.debug(
                    f"Combinando pedidos: {requests[left]} + {requests[right]}"
                )
                left += 1
            else:
                logger.debug(f"Pedido {requests[right]} enviado sozinho")

            right -= 1
            trips += 1

        logger.info(f"Número mínimo de viagens calculado: {trips}")

        return trips


orders_service = OrdersService()
