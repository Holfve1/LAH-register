from app import app

def test_get_all_activities_returns_json_list(web_client, db_connection):
    db_connection.seed("Server/seeds/seed.sql")
    response = web_client.get("/activities")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0
    activity = data[0]
    assert set(activity.keys()) == {"id", "activity"}

def test_get_all_activities_data_matches_seed(web_client, db_connection):
    db_connection.seed("Server/seeds/seed.sql")
    response = web_client.get("/activities")
    data = response.get_json()
    expected = [
        {"id": 1, "activity": "Paintball"},
        {"id": 2, "activity": "Salsa classes"},
        {"id": 3, "activity": "Spanish school"},
    ]
    assert data == expected

def test_activity_gets_created(web_client, db_connection):
    db_connection.seed("Server/seeds/seed.sql")
    response = web_client.post("/activities", json={'activity': 'Dia De La Muerta'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['message'] == 'Activity created successfully'
    # Fetch the updated list and ensure the new activity exists
    updated = web_client.get("/activities").get_json()
    activities = [a['activity'] for a in updated]
    assert 'Dia De La Muerta' in activities

def test_activity_gets_deleted(web_client, db_connection):
    db_connection.seed("Server/seeds/seed.sql")
    response = web_client.delete("/activities/1")
    assert response.status_code == 204 
    updated = web_client.get("/activities").get_json()
    activities = [a["activity"] for a in updated]
    assert "Paintball" not in activities