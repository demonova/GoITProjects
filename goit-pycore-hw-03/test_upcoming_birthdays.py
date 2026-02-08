from datetime import datetime, timedelta

from upcoming_birthdays import get_upcoming_birthdays


def test_upcoming_birthdays_range():
    today = datetime.today().date()
    end_date = today + timedelta(days=7)

    users = [
        {"name": "John Doe", "birthday": "1990.02.10"},
        {"name": "Jane Smith", "birthday": "1985.02.12"},
        {"name": "Charlie", "birthday": "2000.02.13"},
    ]

    result = get_upcoming_birthdays(users)

    for item in result:
        congratulation_date = datetime.strptime(
            item["congratulation_date"], "%Y.%m.%d"
        ).date()

        assert today <= congratulation_date <= end_date

def test_upcoming_birthdays_not_in_past():
    today = datetime.today().date()

    users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
        {"name": "Alice", "birthday": "1990.02.10"},
    ]

    result = get_upcoming_birthdays(users)

    for item in result:
        congratulation_date = datetime.strptime(
            item["congratulation_date"], "%Y.%m.%d"
        ).date()

        assert congratulation_date >= today


def test_congratulation_not_on_weekend():
    users = [
        {"name": "Test User", "birthday": "1990.01.01"},
    ]

    result = get_upcoming_birthdays(users)

    for item in result:
        congratulation_date = datetime.strptime(
            item["congratulation_date"], "%Y.%m.%d"
        ).date()

        assert congratulation_date.weekday() < 5  # 0–4 → пн–пт

def test_result_format():
    users = [
        {"name": "Alice", "birthday": "1990.01.01"},
    ]

    result = get_upcoming_birthdays(users)

    for item in result:
        assert "name" in item
        assert "congratulation_date" in item
        assert isinstance(item["name"], str)

        # проверка формата даты
        datetime.strptime(item["congratulation_date"], "%Y.%m.%d")

def test_return_type():
    users = []

    result = get_upcoming_birthdays(users)

    assert isinstance(result, list)
