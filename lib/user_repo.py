from lib.user import User

class UserRepository:
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM users')
        users = []
        for row in rows:
            item = User(row['id'], row['first_name'], row['last_name'], row['address'])
            users.append(item)
        return users
    def create(self, user):
        self.connection.execute('INSERT INTO users (first_name, last_name, address) VALUES(%s, %s, %s)', [user.first_name, user.last_name, user.address])