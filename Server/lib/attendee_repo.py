from lib.attendee import Attendee

class AttendeeRepository:
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM attendees')
        attendees = []
        for row in rows:
            item = Attendee(row['id'], row['first_name'], row['last_name'], row['suburb'])
            attendees.append(item)
        return attendees
    def create(self, attendee):
        self.connection.execute('INSERT INTO attendees (first_name, last_name, suburb) VALUES(%s, %s, %s)', [attendee.first_name, attendee.last_name, attendee.suburb])