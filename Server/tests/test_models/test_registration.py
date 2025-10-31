from lib.models.registration import Registration

def test_registration_initialises():
    registration = Registration(1, 1, 1)
    assert registration.id == 1
    assert registration.attendee_id == 1
    assert registration.date_id == 1

def test_registrations_are_equal():
    registration1 = Registration(1, 1, 1)
    registration2 = Registration(1, 1, 1)
    assert registration1 == registration2

def test_registrations_are_formatted_correctly():
    registration = Registration(1, 1, 1)
    assert str(registration) == "Registration(1, 1, 1)"