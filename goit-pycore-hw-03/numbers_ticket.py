import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    """
    Generate a sorted list of unique random numbers for a lottery ticket.

    Args:
        min (int): Minimum possible number (>= 1).
        max (int): Maximum possible number (<= 1000).
        quantity (int): Amount of numbers to generate.

    Returns:
        list[int]: Sorted list of unique random numbers or empty list if input is invalid.
    """
    if (min < 1 or max > 1000 or min >= max) or (quantity <= 0 or quantity > (max - min + 1)):
        return []
    else:
        numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)  
