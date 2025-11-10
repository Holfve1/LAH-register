from lib.models.registration import Registration

class RegistrationRepository():
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM registrations ORDER by id')
        registrations = []
        for row in rows:
            item = Registration(row['id'], row['attendee_id'], row['date_id'])
            registrations.append(item)
        return registrations

    def create(self, registration):
        self.connection.execute('INSERT INTO registrations (attendee_id, date_id) VALUES(%s, %s)', [registration.attendee_id, registration.date_id])
        return None
    
    def delete(self, id):
        self.connection.execute('DELETE FROM registrations WHERE id = %s', [id])
        return None
    
    def update(self, id, attendee_id, date_id):
        self.connection.execute('UPDATE registrations SET attendee_id = %s, date_id = %s WHERE id = %s', [attendee_id, date_id, id])
        return None
    