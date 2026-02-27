from typing import Callable, Dict


def caching_fibonacci() -> Callable[[int], int]:
    """
    Create a Fibonacci function with internal caching using closure.

    Returns:
        Callable[[int], int]: Fibonacci function with memoization.
    """
    cache: Dict[int, int] = {}

    def fibonacci(n: int) -> int:
        """
        Compute the n-th Fibonacci number using recursion and caching.

        Args:
            n (int): Index of Fibonacci sequence (n >= 0).

        Returns:
            int: n-th Fibonacci number.

        Raises:
            TypeError: If n is not an integer.
            ValueError: If n is negative.
        """
        if not isinstance(n, int):
            raise TypeError("n must be an integer")

        if n <= 0:
            return 0

        if n == 1:
            return 1

        if n in cache:
            return cache[n]

        # recursion with memoization (critical for O(n) complexity)
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


if __name__ == "__main__":
    fib = caching_fibonacci()

    print(fib(10))  # 55
    print(fib(15))  # 610
