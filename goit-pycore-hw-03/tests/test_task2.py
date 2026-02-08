import pytest

from src.task2 import get_numbers_ticket


def test_valid_ticket_basic():
    result = get_numbers_ticket(1, 49, 6)

    assert isinstance(result, list)
    assert len(result) == 6
    assert result == sorted(result)
    assert len(result) == len(set(result))
    assert all(1 <= n <= 49 for n in result)


@pytest.mark.parametrize(
    "min_val, max_val, quantity",
    [
        (1, 10, 1),
        (1, 10, 10),
        (5, 15, 5),
    ],
)
def test_valid_different_ranges(min_val, max_val, quantity):
    result = get_numbers_ticket(min_val, max_val, quantity)

    assert len(result) == quantity
    assert result == sorted(result)
    assert len(result) == len(set(result))
    assert all(min_val <= n <= max_val for n in result)


@pytest.mark.parametrize(
    "min_val, max_val, quantity",
    [
        (0, 10, 5),       # min < 1
        (1, 1001, 5),     # max > 1000
        (10, 5, 3),       # min >= max
        (1, 10, 0),       # quantity <= 0
        (1, 10, 20),      # quantity > range
    ],
)
def test_invalid_parameters(min_val, max_val, quantity):
    result = get_numbers_ticket(min_val, max_val, quantity)
    assert result == []


def test_randomness_not_constant():
    first = get_numbers_ticket(1, 50, 6)
    second = get_numbers_ticket(1, 50, 6)

    # allow a rare match due to randomness, but generally they should differ
    assert first != second or first == []
