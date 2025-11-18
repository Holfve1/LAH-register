from app import app
from datetime import date

def test_get_all_activities_by_attendee_id(web_client, db_connection):
    db_connection.seed("Server/seeds/seed.sql")
    response = web_client.get("/activities-by-attendee?id=1")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert set(data[0].keys()) == {"activity", "date"}

    expected = [
        {'activity': 'Paintball', 'date': '2025-05-03'}, 
        {'activity': 'Salsa classes', 'date': '2025-05-05'},
        {'activity': 'Salsa classes', 'date': '2025-06-11'}
    ]
    assert data == expected

def test_get_all_attendees_and_their_activities(web_client, db_connection):
    db_connection.seed("Server/seeds/seed.sql")
    response = web_client.get("/attendees-and-activities")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data,list)
    assert len(data) > 0
    for item in data:
        assert set(item.keys()) == {"first_name", "last_name", "activity"}
    
    expected = [
        {'activity': 'Paintball', 'first_name': 'Sam', 'last_name': 'Fell'},
        {'activity': 'Paintball', 'first_name': 'Dave', 'last_name': 'Smith'},
        {'activity': 'Salsa classes', 'first_name': 'John', 'last_name': 'Doe'},  
        {'activity': 'Salsa classes', 'first_name': 'Sarah', 'last_name': 'Dunce'},
        {'activity': 'Salsa classes', 'first_name': 'Dave', 'last_name': 'Smith'},
    ]
    assert data == expected

def test_get_dates_and_attendees_by_activity_id(web_client, db_connection):
    db_connection.seed("Server/seeds/seed.sql")
    response = web_client.get("/dates-and-attendees-by-activity?id=2")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0
    for item in data:
        assert set(item.keys()) == {"date", "first_name", "last_name"}
    
    expected = [
        {'date': '2025-05-05', 'first_name': 'Sarah', 'last_name': 'Dunce'},
        {'date': '2025-05-05', 'first_name': 'Dave', 'last_name': 'Smith'},
        {'date': '2025-06-11', 'first_name': 'John', 'last_name': 'Doe'},
        {'date': '2025-06-11', 'first_name': 'Dave', 'last_name': 'Smith'}
    ]
    assert data == expected

def test_get_all_activities_with_dates_and_attendees(web_client, db_connection):
    db_connection.seed("Server/seeds/seed.sql")
    response = web_client.get("/activities-with-dates-and-attendees")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0
    for item in data:
        assert set(item.keys()) == {"date", "activity", "first_name", "last_name"}
    
    expected = [
        {'date': '2025-05-03', 'activity': 'Paintball', 'first_name': 'Sam', 'last_name': 'Fell'},
        {'date': '2025-05-03', 'activity': 'Paintball', 'first_name': 'Dave', 'last_name': 'Smith'},
        {'date': '2025-05-05', 'activity': 'Salsa classes', 'first_name': 'Sarah', 'last_name': 'Dunce'},
        {'date': '2025-05-05', 'activity': 'Salsa classes', 'first_name': 'Dave', 'last_name': 'Smith'},
        {'date': '2025-06-11', 'activity': 'Salsa classes', 'first_name': 'John', 'last_name': 'Doe'},
        {'date': '2025-06-11', 'activity': 'Salsa classes', 'first_name': 'Dave', 'last_name': 'Smith'},
    ]
    assert data == expected

def test_get_date_with_activities_and_attendees(web_client, db_connection):
    db_connection.seed("Server/seeds/seed.sql")
    response = web_client.get("/date-with-activities-and-attendees?id=1")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0
    for item in data:
        assert set(item.keys()) == {"date", "activity", "first_name", "last_name"}
    
    expected = [
        {'date': '2025-05-03', 'activity': 'Paintball', 'first_name': 'Sam', 'last_name': 'Fell'},
        {'date': '2025-05-03', 'activity': 'Paintball', 'first_name': 'Dave', 'last_name': 'Smith'},
    ]
    assert data == expected

def test_get_all_dates_with_activities_and_attendees(web_client, db_connection):
    db_connection.seed("Server/seeds/seed.sql")
    response = web_client.get("/all-dates-with-activities-and-attendees")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0
    for item in data:
        assert set(item.keys()) == {"date", "activity", "first_name", "last_name"}
    
    expected = [
        
        {'date': '2025-05-03', 'activity': 'Paintball', 'first_name': 'Sam', 'last_name': 'Fell'},
        {'date': '2025-05-03', 'activity': 'Paintball', 'first_name': 'Dave', 'last_name': 'Smith'},
        {'date': '2025-05-05', 'activity': 'Salsa classes', 'first_name': 'Sarah', 'last_name': 'Dunce'},
        {'date': '2025-05-05', 'activity': 'Salsa classes', 'first_name': 'Dave', 'last_name': 'Smith'},
        {'date': '2025-06-11', 'activity': 'Salsa classes', 'first_name': 'John', 'last_name': 'Doe'},
        {'date': '2025-06-11', 'activity': 'Salsa classes', 'first_name': 'Dave', 'last_name': 'Smith'},
    ]
    assert data == expected



