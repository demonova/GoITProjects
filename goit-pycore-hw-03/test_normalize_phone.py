import pytest

from normalize_phone import normalize_phone


@pytest.mark.parametrize(
    "input_phone, expected",
    [
        ("067\\t123 4567", "+380671234567"),
        ("(095) 234-5678\\n", "+380952345678"),
        ("+380 44 123 4567", "+380441234567"),
        ("380501234567", "+380501234567"),
        ("    +38(050)123-32-34", "+380501233234"),
        ("     0503451234", "+380503451234"),
        ("(050)8889900", "+380508889900"),
        ("38050-111-22-22", "+380501112222"),
        ("38050 111 22 11   ", "+380501112211"),
    ]
)
def test_normalize_phone(input_phone, expected):
    assert normalize_phone(input_phone) == expected
