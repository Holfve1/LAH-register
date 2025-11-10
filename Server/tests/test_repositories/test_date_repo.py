
from datetime import date
from lib.models.date import Date
from lib.repositories.date_repo import DateRepository

def test_gets_all_dates(db_connection):
    db_connection.seed("Server/seeds/seed.sql")
    date_repo = DateRepository(db_connection)
    dates = date_repo.all()
    assert dates == [
        Date(1, date(2025, 5, 3), 1),
        Date(2, date(2025, 5, 5), 2),
        Date(3, date(2025, 6, 11), 2),
        Date(4, date(2025, 7, 15), 3),
        Date(5, date(2025, 9, 21), 3),
        Date(6, date(2025, 10, 26), 1),
    ]

def test_creates_date(db_connection):
    db_connection.seed('Server/seeds/seed.sql')
    date_repo = DateRepository(db_connection)
    date_repo.create(Date(None, "2025-05-10", 1))
    dates = date_repo.all()
    assert dates == [
       Date(1, date(2025, 5, 3), 1),
        Date(2, date(2025, 5, 5), 2),
        Date(3, date(2025, 6, 11), 2),
        Date(4, date(2025, 7, 15), 3),
        Date(5, date(2025, 9, 21), 3),
        Date(6, date(2025, 10, 26), 1),
        Date(7, date(2025, 5, 10), 1),
    ]

def test_deletes_date(db_connection):
    db_connection.seed('Server/seeds/seed.sql')
    date_repo = DateRepository(db_connection)
    date_repo.delete(1)
    dates = date_repo.all()
    assert dates == [
        Date(2, date(2025, 5, 5), 2),
        Date(3, date(2025, 6, 11), 2),
        Date(4, date(2025, 7, 15), 3),
        Date(5, date(2025, 9, 21), 3),
        Date(6, date(2025, 10, 26), 1),
    ]

def test_updates_date(db_connection):
    db_connection.seed('Server/seeds/seed.sql')
    date_repo = DateRepository(db_connection)
    date_repo.update(1, "2025-01-20", 2)
    dates = date_repo.all()
    assert dates == [
        Date(1, date(2025, 1, 20), 2),
        Date(2, date(2025, 5, 5), 2),
        Date(3, date(2025, 6, 11), 2),
        Date(4, date(2025, 7, 15), 3),
        Date(5, date(2025, 9, 21), 3),
        Date(6, date(2025, 10, 26), 1)
        
    ]

def test_find_by_date_id(db_connection):
    db_connection.seed('Server/seeds/seed.sql')
    date_repo = DateRepository(db_connection)
    the_date = date_repo.find_by_date_id(2)
    assert the_date == Date(2, date(2025, 5, 5), 2)

    missing_date = date_repo.find_by_date_id(999)
    assert missing_date is None


def test_find_by_activity_id(db_connection):
    db_connection.seed('Server/seeds/seed.sql')
    date_repo = DateRepository(db_connection)
    dates = date_repo.find_by_activity_id(3)
    assert dates == [Date(4, date(2025, 7, 15), 3), Date(5, date(2025, 9, 21), 3)]

    no_dates = date_repo.find_by_activity_id(999)
    assert no_dates == []