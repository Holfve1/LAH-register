from lib.models.date import Date
from lib.repositories.date_repository import DateRepository

def test_gets_all_dates(db_connection):
    db_connection.seed("Server/seeds/seed.sql")
    date_repo = DateRepository(db_connection)
    dates = date_repo.all()
    assert dates == [
        Date(1, "2025-01-15", 1),
        Date(2, "2025-02-20", 2),
        Date(3, "2025-03-25", 3),
        Date(4, "2025-04-30", 4),
    ]

def test_creates_date(db_connection):
    db_connection.seed('Server/seeds/seed.sql')
    date_repo = DateRepository(db_connection)
    date_repo.create(Date(None, "2025-05-10", 1))
    dates = date_repo.all()
    assert dates == [
        Date(1, "2025-01-15", 1),
        Date(2, "2025-02-20", 2),
        Date(3, "2025-03-25", 3),
        Date(4, "2025-04-30", 4),
        Date(5, "2025-05-10", 1)
    ]

def test_deletes_date(db_connection):
    db_connection.seed('Server/seeds/seed.sql')
    date_repo = DateRepository(db_connection)
    date_repo.delete(1)
    dates = date_repo.all()
    assert dates == [
        Date(2, "2025-02-20", 2),
        Date(3, "2025-03-25", 3),
        Date(4, "2025-04-30", 4),
    ]

def test_updates_date(db_connection):
    db_connection.seed('Server/seeds/seed.sql')
    date_repo = DateRepository(db_connection)
    date_repo.update(1, "2025-01-20", 2)
    dates = date_repo.all()
    assert dates == [
        Date(2, "2025-02-20", 2),
        Date(3, "2025-03-25", 3),
        Date(4, "2025-04-30", 4),
        Date(1, "2025-01-20", 2),
    ]

def test_find_by_date_id(db_connection):
    db_connection.seed('Server/seeds/seed.sql')
    date_repo = DateRepository(db_connection)
    date = date_repo.find_by_date_id(2)
    assert date == Date(2, "2025-02-20", 2)

    missing_date = date_repo.find_by_date_id(999)
    assert missing_date is None


def test_find_by_activity_id(db_connection):
    db_connection.seed('Server/seeds/seed.sql')
    date_repo = DateRepository(db_connection)
    dates = date_repo.find_by_activity_id(3)
    assert dates == [Date(3, "2025-03-25", 3)]
    
    no_dates = date_repo.find_by_activity_id(999)
    assert no_dates == []