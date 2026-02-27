# src/task2.py

from typing import List, Dict


def get_cats_info(path: str) -> List[Dict[str, str]]:
    """
    Read cats data from file and return list of dictionaries.

    Each line must be formatted as:
    id,name,age

    Args:
        path (str): Path to cats file.

    Returns:
        List[Dict[str, str]]: List of cats information.
    """
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                try:
                    cat_id, name, age = line.split(",")
                    cats.append(
                        {
                            "id": cat_id,
                            "name": name,
                            "age": age,
                        }
                    )
                except ValueError as exc:
                    print(f"Invalid line format: {line}\nError: {exc}")

    except FileNotFoundError as exc:
        print(f"File {path} not found due to error:\n{exc}")
    except OSError as exc:
        print(f"Cannot open file: {path} due to error:\n{exc}")
    except UnicodeDecodeError as exc:
        print(f"File encoding is invalid due to error:\n{exc}")

    return cats
