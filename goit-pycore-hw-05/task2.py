import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Yield all real numbers from text that are separated by spaces.

    Args:
        text (str): Input string containing numbers.

    Yields:
        float: Extracted real numbers.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    pattern = r"(?<=\s)\d+\.\d+(?=\s|[^\d]|$)"

    for match in re.finditer(pattern, text):
        yield float(match.group())


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Calculate total sum of real numbers in text using provided generator function.

    Args:
        text (str): Input string.
        func (Callable): Generator function extracting numbers.

    Returns:
        float: Total sum of extracted numbers.

    Raises:
        TypeError: If func is not callable.
    """
    if not callable(func):
        raise TypeError("func must be callable")

    return sum(func(text))


if __name__ == "__main__":
    text = (
        "Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими надходженнями "
        "27.45 і 324.00 доларів."
    )

    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income:}")
