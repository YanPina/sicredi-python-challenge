from src.models.orders import OrderRequest
from src.services.orders_svc import orders_service


def test_combine_orders() -> None:
    request = OrderRequest(requests=[70, 50, 80, 50], n_max=100)
    result = orders_service.combine_orders(request)
    expected = 3  # (50+50), (70), (80)
    assert (
        result == expected
    ), f"Erro: esperado {expected}, mas obteve {result}"


def test_combine_orders_all_single_trips() -> None:
    request = OrderRequest(requests=[100, 90, 80, 70], n_max=100)
    result = orders_service.combine_orders(request)
    expected = 4  # Nenhum pode ser combinado, 4 viagens necessárias
    assert (
        result == expected
    ), f"Erro: esperado {expected}, mas obteve {result}"


def test_combine_orders_with_empty_requests() -> None:
    request = OrderRequest(requests=[], n_max=100)
    result = orders_service.combine_orders(request)
    expected = 0  # Nenhuma viagem necessária
    assert (
        result == expected
    ), f"Erro: esperado {expected}, mas obteve {result}"


def test_combine_orders_with_optimal_pairing() -> None:
    request = OrderRequest(requests=[30, 70, 40, 60, 50, 50], n_max=100)
    result = orders_service.combine_orders(request)
    expected = 3  # (30+70), (40+60), (50+50)
    assert (
        result == expected
    ), f"Erro: esperado {expected}, mas obteve {result}"


def test_combine_orders_with_large_n_max() -> None:
    request = OrderRequest(requests=[20, 30, 40, 50, 60], n_max=200)
    result = orders_service.combine_orders(request)
    expected = 3  # (20+60), (30+50), (40)
    assert (
        result == expected
    ), f"Erro: esperado {expected}, mas obteve {result}"
