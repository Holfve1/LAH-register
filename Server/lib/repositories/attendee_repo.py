from lib.models.attendee import Attendee

class AttendeeRepository:
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM attendees ORDER by id')
        attendees = []
        for row in rows:
            item = Attendee(row['id'], row['first_name'], row['last_name'], row['suburb'])
            attendees.append(item)
        return attendees
    
    def find_by_details(self, first_name, last_name, suburb):
        rows = self.connection.execute(
            '''
            SELECT * FROM attendees
            WHERE first_name = %s AND last_name = %s AND suburb = %s
            ''',
            [first_name, last_name, suburb]
        )
        if rows:
            row = rows[0]
            return Attendee(row['id'], row['first_name'], row['last_name'], row['suburb'])
        return None

    def create(self, attendee):
        rows = self.connection.execute(
            'INSERT INTO attendees (first_name, last_name, suburb) VALUES (%s, %s, %s) RETURNING id',
            [attendee.first_name, attendee.last_name, attendee.suburb]
        )
        attendee.id = rows[0]['id']
        return attendee
    
    def delete(self, id):
        self.connection.execute('DELETE FROM attendees WHERE id = %s', [id])
        return None
    
    def update(self, id, first_name, last_name, suburb):
        self.connection.execute('UPDATE attendees SET first_name = %s, last_name = %s, suburb = %s WHERE id = %s', [first_name, last_name, suburb, id])
        return None
    