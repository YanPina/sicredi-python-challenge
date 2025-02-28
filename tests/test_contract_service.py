from src.models.contract import Contract, ContractRequest
from src.services.contract_svc import contract_service


def test_get_top_n_open_contracts() -> None:
    request = ContractRequest(
        open_contracts=[
            Contract(id=1, debt=1.0),
            Contract(id=2, debt=2.0),
            Contract(id=3, debt=3.0),
            Contract(id=4, debt=4.0),
            Contract(id=5, debt=5.0),
        ],
        renegotiated_contracts=[3],
        top_n=3,
    )
    expected = [5, 4, 2]
    result = contract_service.get_top_n_open_contracts(request)
    assert (
        result == expected
    ), f"Erro: esperado {expected}, mas obteve {result}"


def test_get_top_n_open_contracts_with_empty_list() -> None:
    request = ContractRequest(
        open_contracts=[], renegotiated_contracts=[], top_n=3
    )
    result = contract_service.get_top_n_open_contracts(request)
    assert result == [], f"Erro: esperado lista vazia, mas obteve {result}"


def test_get_top_n_open_contracts_with_all_renegotiated() -> None:
    request = ContractRequest(
        open_contracts=[
            Contract(id=1, debt=10.0),
            Contract(id=2, debt=20.0),
            Contract(id=3, debt=30.0),
        ],
        renegotiated_contracts=[1, 2, 3],
        top_n=2,
    )
    result = contract_service.get_top_n_open_contracts(request)
    assert result == [], f"Erro: esperado lista vazia, mas obteve {result}"


def test_get_top_n_open_contracts_with_top_n_greater_than_list() -> None:
    request = ContractRequest(
        open_contracts=[
            Contract(id=1, debt=100.0),
            Contract(id=2, debt=200.0),
        ],
        renegotiated_contracts=[],
        top_n=5,
    )
    expected = [2, 1]
    result = contract_service.get_top_n_open_contracts(request)
    assert (
        result == expected
    ), f"Erro: esperado {expected}, mas obteve {result}"
