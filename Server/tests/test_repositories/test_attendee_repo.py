
# from lib.models.attendee import Attendee
# from lib.attendee_repo import AttendeeRepository
# from lib.database_connection import DatabaseConnection

# def test_gets_all_attendees(db_connection):
#     db_connection.seed("Server/seeds/attendees.sql")
#     attendee_repo = AttendeeRepository(db_connection)
#     attendees = attendee_repo.all()
#     assert attendees == [
#             Attendee(1, 'Dave', 'Smith', 'Camden'),
#             Attendee(2, 'Sam', 'Fell', 'Kilburn'),
#             Attendee(3, 'John', 'Doe', 'Westminster'),
#             Attendee(4, 'Sarah', 'Dunce', 'Elephant & Castle'),
#     ]


# def test_find_an_attendee(db_connection):
#     db_connection.seed("Server/seeds/attendees.sql")
#     attendee_repo = AttendeeRepository(db_connection)
#     attendee = attendee_repo.find("Dave", "Smith")
#     assert attendee == Attendee(1, "Dave", "Smith", "Camden")