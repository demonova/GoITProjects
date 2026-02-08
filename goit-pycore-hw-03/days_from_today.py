from datetime import datetime, date


def get_days_from_today(date_str: str) -> int:
    """
    Calculate the number of days between the given date and today.

    Args:
        date_str (str): Date in 'YYYY-MM-DD' format.

    Returns:
        int: Number of days from the given date to today.
             Negative if the given date is in the future.

    Raises:
        ValueError: If the input date string has an invalid format.
    """
    try:
        return (date.today() - datetime.strptime(date_str, "%Y-%m-%d").date()).days
    except ValueError as exc:
        raise ValueError(
            f"Invalid date format. Expected 'YYYY-MM-DD'. Input: {date_str}"
        ) from exc
