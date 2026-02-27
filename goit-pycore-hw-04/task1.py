from typing import Tuple


def total_salary(path: str) -> Tuple[int, float]:
    """
    Calculate total and average salary from a file.

    Each line in file must be formatted as:
    Name,SALARY

    Args:
        path (str): Path to salary file.

    Returns:
        Tuple[int, int]: (total_salary, average_salary)
    """
    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                try:
                    _, salary = line.split(",")
                    count += 1
                    total += int(salary)
                except ValueError as exc:
                    print(f"Invalid line format: {line}\nError: {exc}")

    except FileNotFoundError as exc:
        print(f"File {path} not found due to error:\n{exc}")
    except OSError as exc:
        print(f"Cannot open file: {path} due to error:\n{exc}")
    except UnicodeDecodeError as exc:
        print(f"File encoding is invalid due to error:\n{exc}")

    if count == 0:
        return total, count

    average = total // count
    return total, average
