from lib.models.attendee import Attendee

def test_attendee_initialises():
    attendee = Attendee(1, "Dave", "Smith", "Camden")
    assert attendee.first_name == "Dave"
    assert attendee.last_name == "Smith"
    assert attendee.suburb == "Camden"

def test_attendees_are_equal():
    attendee1 = Attendee(1, "Dave", "Smith", "Camden")
    attendee2 = Attendee(1, "Dave", "Smith", "Camden")
    assert attendee1 == attendee2

def test_attendees_are_formatted_correctly():
    attendee = Attendee(1, "Dave", "Smith", "Camden")
    assert str(attendee) == "Attendee(1, Dave, Smith, Camden)"