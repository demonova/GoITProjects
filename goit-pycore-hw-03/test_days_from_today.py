import pytest
from datetime import date, timedelta

from days_from_today import get_days_from_today


@pytest.mark.parametrize("bad_date", [
    "2020/10/09",
    "09-10-2020",
    "2020-13-01",
    "abc",
    "",
])
def test_invalid_formats(bad_date):
    with pytest.raises(ValueError):
        get_days_from_today(bad_date)


@pytest.mark.parametrize("date_str, expected", [
    ((date.today()).strftime("%Y-%m-%d"), 0),
    ((date.today() - timedelta(days=1)).strftime("%Y-%m-%d"), 1),
    ((date.today() + timedelta(days=1)).strftime("%Y-%m-%d"), -1),
])
def test_valid_dates(date_str, expected):
    assert get_days_from_today(date_str) == expected


def test_past_date():
    past_date = (date.today() - timedelta(days=10)).strftime("%Y-%m-%d")
    assert get_days_from_today(past_date) == 10


def test_future_date():
    future_date = (date.today() + timedelta(days=10)).strftime("%Y-%m-%d")
    assert get_days_from_today(future_date) == -10


@pytest.mark.parametrize("invalid_date", [
    "2020-02-30",
    "2021-04-31",
    "2020-00-01",
])
def test_invalid_calendar_dates(invalid_date):
    with pytest.raises(ValueError):
        get_days_from_today(invalid_date)
