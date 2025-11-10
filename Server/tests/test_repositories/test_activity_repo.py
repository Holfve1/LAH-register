from lib.models.activity import Activity
from lib.repositories.activity_repo import ActivityRepository

def test_gets_all_activities(db_connection):
    db_connection.seed('Server/seeds/seed.sql')
    activitiy_repo = ActivityRepository(db_connection)
    activities = activitiy_repo.all()
    assert activities == [
            Activity(1, 'Paintball'),
            Activity(2, 'Salsa classes'),
            Activity(3, 'Spanish school')
    ]

def test_create_activity(db_connection):
    db_connection.seed('Server/seeds/seed.sql')
    activity_repo = ActivityRepository(db_connection)
    activity_repo.create(Activity(None, 'Food Festival'))
    activities = activity_repo.all()
    assert activities == [
            Activity(1, 'Paintball'),
            Activity(2, 'Salsa classes'),
            Activity(3, 'Spanish school'),
            Activity(4, 'Food Festival')
    ]

def test_deletes_activity(db_connection):
    db_connection.seed('Server/seeds/seed.sql')
    activity_repo = ActivityRepository(db_connection)
    activity_repo.delete(1)
    activities = activity_repo.all()
    assert activities == [
            Activity(2, 'Salsa classes'),
            Activity(3, 'Spanish school')
    ]
def test_updates_activity(db_connection):
    db_connection.seed('Server/seeds/seed.sql')
    activity_repo = ActivityRepository(db_connection)
    activity_repo.update(1, 'Ice Skating')
    activities = activity_repo.all()
    assert activities == [
            Activity(1, 'Ice Skating'),
            Activity(2, 'Salsa classes'),
            Activity(3, 'Spanish school')
            
    ]
