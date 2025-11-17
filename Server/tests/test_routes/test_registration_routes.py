from app import app


def test_get_all_registrations_returns_json_list(web_client, db_connection):
    db_connection.seed("Server/seeds/seed.sql")
    response = web_client.get("/registrations")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0
    registration = data[0]
    assert set(registration.keys()) == {'id', 'date_id', 'attendee_id'}


def test_get_all_registartions_data_matches_seed(web_client, db_connection):
    db_connection.seed("Server/seeds/seed.sql")
    response = web_client.get("/registrations")
    data = response.get_json()
    expected = [
        {"id": 1, "attendee_id": 1, "date_id": 1},
        {"id": 2, "attendee_id": 1, "date_id": 2},
        {"id": 3, "attendee_id": 1, "date_id": 3},
        {"id": 4, "attendee_id": 2, "date_id": 1},
        {"id": 5, "attendee_id": 3, "date_id": 3},
        {"id": 6, "attendee_id": 4, "date_id": 2},
    ]
    assert data == expected


def test_registration_gets_created(web_client, db_connection):
    db_connection.seed("Server/seeds/seed.sql")
    response = web_client.post("/registrations", json={
        'attendee_id': '4',
        'date_id': '4',
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['message'] == 'Registration created successfully'
    updated = web_client.get("/registrations").get_json()
    registrations = [f"{a['attendee_id']}, {a['date_id']}" for a in updated]
    assert '4, 4' in registrations

def test_registration_gets_deleted(web_client, db_connection):
    db_connection.seed('Server/seeds/seed.sql')
    response = web_client.delete('/registrations/1')
    assert response.status_code == 204 
    updated = web_client.get('/registrations').get_json()
    registration = [f"{a['attendee_id']}, {a['date_id']}" for a in updated]
    assert "1, 1" not in registration

def test_registration_gets_updated(web_client, db_connection):
    db_connection.seed('Server/seeds/seed.sql')
    response = web_client.patch('/registrations/1', json={'attendee_id': 1, 'date_id': 4})
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Registration updated successfully'
    updated = web_client.get('/registrations').get_json()
    assert updated[0]['date_id'] == 4