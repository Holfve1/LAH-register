
from lib.models.attendee import Attendee
from lib.repositories.attendee_repo import AttendeeRepository

def test_gets_all_attendees(db_connection):
    db_connection.seed("Server/seeds/seed.sql")
    attendee_repo = AttendeeRepository(db_connection)
    attendees = attendee_repo.all()
    assert attendees == [
            Attendee(1, 'Dave', 'Smith', 'Camden'),
            Attendee(2, 'Sam', 'Fell', 'Kilburn'),
            Attendee(3, 'John', 'Doe', 'Westminster'),
            Attendee(4, 'Sarah', 'Dunce', 'Elephant & Castle'),
    ]
     
def test_creates_attendee(db_connection):
    db_connection.seed('Server/seeds/seed.sql')
    attendee_repo = AttendeeRepository(db_connection)
    attendee_repo.create(Attendee(None, 'Chris', 'Samson', 'Camden'))
    attendees = attendee_repo.all()
    assert attendees == [
            Attendee(1, 'Dave', 'Smith', 'Camden'),
            Attendee(2, 'Sam', 'Fell', 'Kilburn'),
            Attendee(3, 'John', 'Doe', 'Westminster'),
            Attendee(4, 'Sarah', 'Dunce', 'Elephant & Castle'),
            Attendee(5, 'Chris', 'Samson', 'Camden')
    ]

def test_deletes_attendee(db_connection):
    db_connection.seed('Server/seeds/seed.sql')
    attendee_repo = AttendeeRepository(db_connection)
    attendee_repo.delete(1)
    attendees = attendee_repo.all()
    assert attendees == [
            Attendee(2, 'Sam', 'Fell', 'Kilburn'),
            Attendee(3, 'John', 'Doe', 'Westminster'),
            Attendee(4, 'Sarah', 'Dunce', 'Elephant & Castle'),
    ]

def test_updates_attendee(db_connection):
    db_connection.seed('Server/seeds/seed.sql')
    attendee_repo = AttendeeRepository(db_connection)
    attendee_repo.update(1, 'David', 'Smith', 'Camden')
    attendees = attendee_repo.all()
    assert attendees == [
            Attendee(1, 'David', 'Smith', 'Camden'),
            Attendee(2, 'Sam', 'Fell', 'Kilburn'),
            Attendee(3, 'John', 'Doe', 'Westminster'),
            Attendee(4, 'Sarah', 'Dunce', 'Elephant & Castle')
            
    ]