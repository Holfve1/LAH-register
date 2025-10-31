from lib.models.date import Date

class DateRepository:
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM dates')
        dates = []
        for row in rows:
            item = Date(row['id'], row['date'], row['activity_id'])
            dates.append(item)
        return dates

    def create(self, date):
        self.connection.execute('INSERT INTO dates (date, activity_id) VALUES(%s, %s)', [date.date, date.activity_id])
        return None
    
    def delete(self, id):
        self.connection.execute('DELETE FROM dates WHERE id = %s', [id])
        return None
    
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
