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