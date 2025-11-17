
from lib.models.registration import Registration
from lib.repositories.registration_repo import RegistrationRepository

def test_gets_all_registrations(db_connection):
    db_connection.seed("Server/seeds/seed.sql")
    registration_repo = RegistrationRepository(db_connection)
    registrations = registration_repo.all()
    assert registrations == [
                Registration(1, 1, 1),
                Registration(2, 1, 2),
                Registration(3, 1, 3),
                Registration(4, 2, 1),
                Registration(5, 3, 3),
                Registration(6, 4, 2)
    ]
     
def test_creates_registartions(db_connection):
    db_connection.seed('Server/seeds/seed.sql')
    registration_repo = RegistrationRepository(db_connection)
    registration_repo.create(Registration(None, 3, 3))
    registrations = registration_repo.all()
    assert registrations == [
                Registration(1, 1, 1),
                Registration(2, 1, 2),
                Registration(3, 1, 3),
                Registration(4, 2, 1),
                Registration(5, 3, 3),
                Registration(6, 4, 2),
                Registration(7, 3, 3)
    ]

def test_deletes_attendee(db_connection):
    db_connection.seed('Server/seeds/seed.sql')
    registration_repo = RegistrationRepository(db_connection)
    registration_repo.delete(1)
    registrations = registration_repo.all()
    assert registrations == [
                Registration(2, 1, 2),
                Registration(3, 1, 3),
                Registration(4, 2, 1),
                Registration(5, 3, 3),
                Registration(6, 4, 2)
    ]

def test_updates_attendee(db_connection):
    db_connection.seed('Server/seeds/seed.sql')
    registration_repo = RegistrationRepository(db_connection)
    registration_repo.update(1, 3, 3)
    registrations = registration_repo.all()
    assert registrations == [
                Registration(1, 3, 3),
                Registration(2, 1, 2),
                Registration(3, 1, 3),
                Registration(4, 2, 1),
                Registration(5, 3, 3),
                Registration(6, 4, 2)
                
    ]