from collections import UserDict
from datetime import datetime, timedelta


# =========================
# Models
# =========================

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not (value.isdigit() and len(value) == 10):
            raise ValueError("Phone must contain exactly 10 digits.")
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value):
        try:
            date = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        super().__init__(date)

    def __str__(self):
        return self.value.strftime("%d.%m.%Y")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        phone_obj = self.find_phone(phone)
        if phone_obj:
            self.phones.remove(phone_obj)

    def edit_phone(self, old_phone, new_phone):
        phone_obj = self.find_phone(old_phone)

        if not phone_obj:
            raise ValueError("Phone not found.")
        
        self.phones.remove(phone_obj)
        self.phones.append(Phone(new_phone))

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
            
        return None

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def __str__(self):
        phones = "; ".join(p.value for p in self.phones)
        birthday = f", birthday: {self.birthday}" if self.birthday else ""
        
        return f"Contact name: {self.name.value}, phones: {phones}{birthday}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        end_date = today + timedelta(days=7)

        upcoming_birthdays = []

        for record in self.data.values():
            if not record.birthday:
                continue

            birthday = record.birthday.value.date()            
            
            # Handle leap year birthdays (February 29)
            try:
                birthday_this_year = birthday.replace(year=today.year)
            except ValueError:
                # If the date is February 29 in a non-leap year, set it to February 28
                birthday_this_year = birthday.replace(year=today.year, day=28)

            if birthday_this_year < today:
                try:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)
                except ValueError:
                    birthday_this_year = birthday.replace(year=today.year + 1, day=28)
            
            if today <= birthday_this_year <= end_date:
                congratulation_date = birthday_this_year

                if congratulation_date.weekday() == 5:  # Saturday
                    congratulation_date += timedelta(days=2)
                elif congratulation_date.weekday() == 6:  # Sunday
                    congratulation_date += timedelta(days=1)

                upcoming_birthdays.append(
                    {
                        "name": record.name.value,
                        "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
                    }
                )

        return upcoming_birthdays

# =========================
# CLI
# =========================

def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except ValueError as e:
            return str(e)
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Invalid command format."

    return inner


@input_error
def add_contact(args, book):
    name, phone, *_ = args
    record = book.find(name)

    # If contact doesn't exist, create a new one
    if record is None:
        record = Record(name)
        book.add_record(record)
        record.add_phone(phone)
    
        return "Contact added."
    
    if phone:
        record.add_phone(phone)

    return "Contact updated."


@input_error
def change_contact(args, book):
    name, old_phone, new_phone = args
    record = book.find(name)

    if not record:
        raise KeyError

    record.edit_phone(old_phone, new_phone)

    return "Phone updated."


@input_error
def show_phone(args, book):
    name = args[0]
    record = book.find(name)

    if not record:
        raise KeyError

    return "; ".join(p.value for p in record.phones)


@input_error
def show_all(book):
    return "\n".join(str(record) for record in book.data.values())


@input_error
def add_birthday(args, book):
    name, birthday = args
    record = book.find(name)

    if not record:
        raise KeyError

    record.add_birthday(birthday)

    return "Birthday added."


@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)

    if not record:
        raise KeyError

    if not record.birthday:
        return "Birthday not set."

    return str(record.birthday)


@input_error
def birthdays(book):
    upcoming = book.get_upcoming_birthdays()

    if not upcoming:
        return "No upcoming birthdays."

    return "\n".join(
        f"{u['name']} -> {u['congratulation_date']}"
        for u in upcoming
    )


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        if not user_input:
            continue

        command, *args = user_input.strip().split()

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_all(book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(book))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
