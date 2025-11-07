from lib.models.attendee import Attendee
from lib.models.activity import Activity
from lib.models.date import Date
from lib.models.registration import Registration
from lib.repositories.join_repo import JoinRepository

def test_find_activities_by_attendee_id(db_connection):
    db_connection.seed("Server/seeds/seed.sql")
    join_repo = JoinRepository(db_connection)
    attendee = join_repo.find_activities_by_attendee_id(1)
    assert attendee == [
                        {'activity': 'Paintball', 'date': '2025-05-03'}, 
                        {'activity': 'Salsa classes', 'date': '2025-05-05'},
                        {'activity': 'Salsa classes', 'date': '2025-06-11'}
    ]

def test_all_attendees_with_activities(db_connection):
    db_connection.seed("Server/seeds/seed.sql")
    join_repo = JoinRepository(db_connection)
    attendees = join_repo.all_attendees_with_activities()
    assert attendees == [
                        {'activity': 'Paintball', 'first_name': 'Sam', 'last_name': 'Fell'},
                        {'activity': 'Paintball', 'first_name': 'Dave', 'last_name': 'Smith'},
                        {'activity': 'Salsa classes', 'first_name': 'John', 'last_name': 'Doe'},  
                        {'activity': 'Salsa classes', 'first_name': 'Sarah', 'last_name': 'Dunce'},
                        {'activity': 'Salsa classes', 'first_name': 'Dave', 'last_name': 'Smith'}
                        
]

def test_find_dates_and_attendees_by_activity_id(db_connection):
    db_connection.seed("Server/seeds/seed.sql")
    join_repo = JoinRepository(db_connection)
    dates_and_attendees = join_repo.find_dates_and_attendees_by_activity_id(2)
    assert dates_and_attendees == [
                        {'date': '2025-05-05', 'first_name': 'Sarah', 'last_name': 'Dunce'},
                        {'date': '2025-05-05', 'first_name': 'Dave', 'last_name': 'Smith'},
                        {'date': '2025-06-11', 'first_name': 'John', 'last_name': 'Doe'},
                        {'date': '2025-06-11', 'first_name': 'Dave', 'last_name': 'Smith'}
    ]

def test_all_activities_with_dates_and_attendees(db_connection):
    db_connection.seed("Server/seeds/seed.sql")
    join_repo = JoinRepository(db_connection)
    activities_dates_attendees = join_repo.all_activities_with_dates_and_attendees()
    assert activities_dates_attendees == [
        {'date': '2025-05-03', 'activity': 'Paintball', 'first_name': 'Sam', 'last_name': 'Fell'},
        {'date': '2025-05-03', 'activity': 'Paintball', 'first_name': 'Dave', 'last_name': 'Smith'},
        {'date': '2025-05-05', 'activity': 'Salsa classes', 'first_name': 'Sarah', 'last_name': 'Dunce'},
        {'date': '2025-05-05', 'activity': 'Salsa classes', 'first_name': 'Dave', 'last_name': 'Smith'},
        {'date': '2025-06-11', 'activity': 'Salsa classes', 'first_name': 'John', 'last_name': 'Doe'},
        {'date': '2025-06-11', 'activity': 'Salsa classes', 'first_name': 'Dave', 'last_name': 'Smith'},
        
    ]


def test_find_date_with_activities_and_attendees(db_connection):
    db_connection.seed("Server/seeds/seed.sql")
    join_repo = JoinRepository(db_connection)
    date_activities_attendees = join_repo.find_date_with_activities_and_attendees(1)
    assert date_activities_attendees == [
        {'date': '2025-05-03', 'activity': 'Paintball', 'first_name': 'Sam', 'last_name': 'Fell'},
        {'date': '2025-05-03', 'activity': 'Paintball', 'first_name': 'Dave', 'last_name': 'Smith'},
    ]

def test_all_dates_with_activities_and_attendees(db_connection):
    db_connection.seed("Server/seeds/seed.sql")
    join_repo = JoinRepository(db_connection)
    dates_activities_attendees = join_repo.all_dates_with_activities_and_attendees()
    assert dates_activities_attendees == [
        
        {'date': '2025-05-03', 'activity': 'Paintball', 'first_name': 'Sam', 'last_name': 'Fell'},
        {'date': '2025-05-03', 'activity': 'Paintball', 'first_name': 'Dave', 'last_name': 'Smith'},

        {'date': '2025-05-05', 'activity': 'Salsa classes', 'first_name': 'Sarah', 'last_name': 'Dunce'},
        {'date': '2025-05-05', 'activity': 'Salsa classes', 'first_name': 'Dave', 'last_name': 'Smith'},
        
        {'date': '2025-06-11', 'activity': 'Salsa classes', 'first_name': 'John', 'last_name': 'Doe'},
        {'date': '2025-06-11', 'activity': 'Salsa classes', 'first_name': 'Dave', 'last_name': 'Smith'},
        
    ]


