from lib.models.date import Date

def test_date_initialises():
    date = Date(1, "2025-10-29", 1)
    assert date.id == 1
    assert date.date == "2025-10-29"
    assert date.activity_id == 1

def test_dates_are_equal():
    date1 = Date(1, "2025-10-29", 1)
    date2 = Date(1, "2025-10-29", 1)
    assert date1 == date2

def test_dates_are_formatted_correctly():
    date = Date(1, "2025-10-29", 1)
    assert str(date) == "Date(1, 2025-10-29, 1)"