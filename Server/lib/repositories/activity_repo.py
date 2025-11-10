from lib.models.activity import Activity

class ActivityRepository():
    def __init__(self, connection):
        self.connection  = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM activities ORDER by id')
        activities = []
        for row in rows:
            item = Activity(row['id'], row['activity'])
            activities.append(item)
        return activities 


    def create(self, activity):
        self.connection.execute('INSERT INTO activities (activity) VALUES (%s)', [activity.activity])
        return None 
        

    def delete(self, id):
        self.connection.execute('DELETE FROM activities WHERE id = %s', [id])
        return None

    def update(self, id, activity):
        self.connection.execute('UPDATE activities SET activity = %s WHERE id = %s', [activity, id])
        return None