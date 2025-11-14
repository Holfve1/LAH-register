from app import app
from datetime import date


def test_get_all_dates_returns_json_list(web_client, db_connection):
    # Arrange: seed the database
    db_connection.seed("Server/seeds/seed.sql")

    # Act: make a GET request to the route
    response = web_client.get("/dates")

    assert response.status_code == 200

    # Assert: response is JSON and a list
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0

    # Assert: first item has the right structure - set checks that the dictionary has exactly the right fields, in any order
    date = data[0]
    assert set(date.keys()) == {"id", "date", "activity_id"}


def test_get_all_dates_data_matches_seed(web_client, db_connection):
    db_connection.seed("Server/seeds/seed.sql")

    response = web_client.get("/dates")
    data = response.get_json()

    expected = [
        {"id": 1, "date": "2025-05-03", "activity_id": 1},
        {"id": 2, "date": "2025-05-05", "activity_id": 2},
        {"id": 3, "date": "2025-06-11", "activity_id": 2},
        {"id": 4, "date": "2025-07-15", "activity_id": 3},
        {"id": 5, "date": "2025-09-21", "activity_id": 3},
        {"id": 6, "date": "2025-10-26", "activity_id": 1}
    ]

    assert data == expected

def test_date_gets_created(web_client, db_connection):
    db_connection.seed("Server/seeds/seed.sql")
    response = web_client.post("/dates", json={
        'date': '2025-12-31',
        'activity_id': 2
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['message'] == 'Date created successfully'
    # Fetch the updated list and ensure the new date exists
    updated = web_client.get("/dates").get_json()
    dates = [d['date'] for d in updated]
    assert '2025-12-31' in dates

def test_date_gets_deleted(web_client, db_connection):
    db_connection.seed('Server/seeds/seed.sql')
    response = web_client.delete('/dates/1')
    assert response.status_code == 204 
    updated = web_client.get('/dates').get_json()
    dates = [d['date'] for d in updated]
    assert "2025-05-03" not in dates

def test_date_gets_updated(web_client, db_connection):
    db_connection.seed('Server/seeds/seed.sql')
    response = web_client.patch("/dates/1", json={
        'date': '2025-05-04',
        'activity_id': 1
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Date updated successfully'
    updated = web_client.get('/dates').get_json()
    assert updated[0]['date'] == '2025-05-04'