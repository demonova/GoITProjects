import re


def normalize_phone(phone_number: str) -> str:
    """
    Normalize a phone number to international format for Ukraine (+380).

    Args:
        phone_number (str): Raw phone number in any format.

    Returns:
        str: Normalized phone number starting with '+380'.

    Raises:
        ValueError: If phone number is empty or invalid.
    """
    
    cleaned = re.sub(r"[^\d+]", "", phone_number.strip())

    if cleaned.startswith("+380"):
        return cleaned

    if cleaned.startswith("380"):
        return f"+{cleaned}"

    if cleaned.startswith("0"):
        return f"+38{cleaned}"

    return f"+38{cleaned}"
