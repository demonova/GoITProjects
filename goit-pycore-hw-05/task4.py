from typing import Callable, Dict, List


def input_error(func: Callable) -> Callable:
    """
    Decorator for handling input-related errors in command handlers.
    """

    def inner(*args, **kwargs) -> str:
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter user name."

    return inner


@input_error
def add_contact(args: List[str], contacts: Dict[str, str]) -> str:
    if len(args) != 2:
        raise ValueError
    
    name, phone = args
    contacts[name] = phone

    return "Contact added."


@input_error
def change_contact(args: List[str], contacts: Dict[str, str]) -> str:
    name, phone = args
    if name not in contacts:
        raise KeyError
    
    contacts[name] = phone

    return "Contact updated."


@input_error
def show_phone(args: List[str], contacts: Dict[str, str]) -> str:
    if not args:
        raise IndexError

    if len(args) != 1:
        raise ValueError

    name = args[0]

    if name not in contacts:
        raise KeyError

    return f"{name}: {contacts[name]}"

@input_error
def show_all(_: List[str], contacts: Dict[str, str]) -> str:
    if not contacts:
        return "No contacts saved."
    
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def parse_input(user_input: str):
    parts = user_input.strip().split()
    if not parts:
        return "", []

    command = parts[0].lower()
    args = parts[1:]

    return command, args

def main() -> None:
    contacts: Dict[str, str] = {}

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")

        if not user_input:
            continue

        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(args, contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
