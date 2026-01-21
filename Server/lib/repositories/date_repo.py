from lib.models.date import Date

class DateRepository:
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM dates ORDER by id')
        dates = []
        for row in rows:
            item = Date(row['id'], row['date'], row['activity_id'])
            dates.append(item)
        return dates
    
    def create(self, date):
        rows = self.connection.execute(
            'INSERT INTO dates (date, activity_id) VALUES (%s, %s) RETURNING id',
            [date.date, date.activity_id]
        )
        date.id = rows[0]['id']
        return date
    
    def update(self, id, date, activity_id):
        self.connection.execute('UPDATE dates SET date = %s, activity_id = %s WHERE id = %s', [date, activity_id, id])
        return None

    
    def find_by_date_id(self, date_id):
        rows = self.connection.execute('SELECT * FROM dates WHERE id = %s', [date_id])
        if rows:
            row = rows[0]
            return Date(row['id'], row['date'], row['activity_id'])
        return None


    def find_by_activity_id(self, activity_id):
        rows = self.connection.execute('SELECT * FROM dates WHERE activity_id = %s', [activity_id])
        dates = []
        for row in rows:
            item = Date(row['id'], row['date'], row['activity_id'])
            dates.append(item)
        return dates

    def find_by_date_and_activity_id(self, date_value, activity_id):
        rows = self.connection.execute(
            '''
            SELECT * FROM dates
            WHERE date = %s AND activity_id = %s
            ''',
            [date_value, activity_id]
        )
        if rows:
            row = rows[0]
            return Date(row['id'], row['date'], row['activity_id'])
        return None