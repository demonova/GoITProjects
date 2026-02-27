#!/usr/bin/env python3
"""
CLI Assistant Bot
"""


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return cmd, *args


def add_contact(args: list, contacts: dict) -> str:
    if len(args) != 2:
        return "Invalid command."
    
    name, phone = args
    contacts[name] = phone
    
    return "Contact added."


def change_contact(args: list, contacts: dict) -> str:
    if len(args) != 2:
        return "Invalid command."
    
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    
    return "Contact not found."


def show_phone(args: list, contacts: dict) -> str:
    if len(args) != 1:
        return "Invalid command."
    
    name = args[0]
    if name in contacts:
        return contacts[name]
    
    return "Contact not found."


def show_all(contacts: dict) -> str:
    if not contacts:
        return "No contacts saved."
    
    return "\n".join(f"{name} {phone}" for name, phone in contacts.items())


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

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
            print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()  
