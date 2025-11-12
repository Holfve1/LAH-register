from app import app

def test_get_all_attendees_returns_json_list(web_client, db_connection):
    # Arrange: seed the database
    db_connection.seed("Server/seeds/seed.sql")

    # Act: make a GET request to the route
    response = web_client.get("/attendees")

    assert response.status_code == 200

    # Assert: response is JSON and a list
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0

    # Assert: first item has the right structure - set checks that the dictionary has exactly the right fields, in any order
    attendee = data[0]
    assert set(attendee.keys()) == {"id", "first_name", "last_name", "suburb"}

def test_get_all_attendees_data_matches_seed(web_client, db_connection):
   
    db_connection.seed("Server/seeds/seed.sql")

    response = web_client.get("/attendees")
    data = response.get_json()

    expected = [
        {"id": 1, "first_name": "Dave", "last_name": "Smith", "suburb": "Camden"},
        {"id": 2, "first_name": "Sam", "last_name": "Fell", "suburb": "Kilburn"},
        {"id": 3, "first_name": "John", "last_name": "Doe", "suburb": "Westminster"},
        {"id": 4, "first_name": "Sarah", "last_name": "Dunce", "suburb": "Elephant & Castle"}
    ]

    assert data == expected

def test_antendee_gets_created(web_client, db_connection):
    db_connection.seed("Server/seds/seed.sql")
    response = web_client.post("/attendees", json={
        'first_name': 'Alice',
        'last_name': 'Johnson',
        'suburb': 'Chelsea'
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['message'] == 'Attendee created successfully'
    # Fetch the updated list and ensure the new attendee exists
    updated = web_client.get("/attendees").get_json()
    attendees = [f"{a['first_name']} {a['last_name']}" for a in updated]
    assert 'Alice Johnson' in attendees

def test_activity_gets_deleted(web_client, db_connection):
    db_connection.seed('Server/seeds/seed.sql')
    response = web_client.delete('/attendees/1')
    assert response.status_code == 204 
    updated = web_client.get('/attendees').get_json()
    attendees = [f"{a['first_name']} {a['last_name']}" for a in updated]
    assert "Dave Smith" not in attendees

def test_attendee_gets_updated(web_client, db_connection):
    db_connection.seed('Server/seeds/seed.sql')
    response = web_client.patch('/attendees/1', json={
        'first_name': 'David',
        'last_name': 'Smithers',
        'suburb': 'Camden Town'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Attendee updated successfully'
    updated = web_client.get('/attendees').get_json()
    attendee = next(a for a in updated if a['id'] == 1)
    assert attendee['first_name'] == 'David'
    assert attendee['last_name'] == 'Smithers'
    assert attendee['suburb'] == 'Camden Town'