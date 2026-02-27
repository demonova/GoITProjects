#!/usr/bin/env python3
"""
Visualize directory structure with indentation and colors.

Usage:
    python task3.py /path/to/directory
"""

import sys
from pathlib import Path
from colorama import Fore, Style, init


def print_structure(directory: Path, level: int = 0) -> None:
    """
    Recursively print directory structure with indentation.

    Directories are blue.
    Files are green.
    """
    indent = " " * 4 * level

    for item in sorted(directory.iterdir(), key=lambda x: x.name.lower()):
        if item.is_dir():
            print(f"{indent}{Fore.BLUE}{item.name}/{Style.RESET_ALL}")
            print_structure(item, level + 1)
        else:
            print(f"{indent}{Fore.GREEN}{item.name}{Style.RESET_ALL}")


def main() -> None:
    init(autoreset=True)

    if len(sys.argv) != 2:
        print("Usage: python task3.py /path/to/directory")
        sys.exit(1)

    path = Path(sys.argv[1])

    if not path.exists():
        print(f"{Fore.RED}Error: Path does not exist.{Style.RESET_ALL}")
        sys.exit(1)

    if not path.is_dir():
        print(f"{Fore.RED}Error: Provided path is not a directory.{Style.RESET_ALL}")
        sys.exit(1)

    print(f"{Fore.CYAN}{path.name}/{Style.RESET_ALL}")
    print_structure(path)


if __name__ == "__main__":
    main()
