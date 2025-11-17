def test_export_all_activities_to_csv(web_client, db_connection):
    db_connection.seed("Server/seeds/seed.sql")
    response = web_client.get("/activities/export")
    assert response.status_code == 200

    # Correct headers
    assert response.mimetype == "text/csv"
    assert "attachment; filename=activities.csv" in response.headers["Content-Disposition"]

    # Body should be plain text, not JSON
    csv_text = response.data.decode("utf-8")

    # Header row must be present
    assert "id,activity" in csv_text

    # Check that at least one seeded activity appears
    # Adjust the names depending on your seed file
    assert "1,Paintball" in csv_text   # ensures an ID row exists

def test_export_all_attendees_to_csv(web_client, db_connection):
    db_connection.seed("Server/seeds/seed.sql")
    response = web_client.get("/attendees/export")
    assert response.status_code == 200
    assert response.mimetype == "text/csv"
    assert "attachment; filename=attendees.csv" in response.headers["Content-Disposition"]
    csv_text = response.data.decode("utf-8")
    assert "id,first_name,last_name,suburb" in csv_text
    assert "1,Dave,Smith,Camden" in csv_text  

def test_export_all_dates_to_csv(web_client, db_connection):
    db_connection.seed("Server/seeds/seed.sql")
    response = web_client.get("/dates/export")
    assert response.status_code == 200
    assert response.mimetype == "text/csv"
    assert "attachment; filename=dates.csv" in response.headers["Content-Disposition"]
    csv_text = response.data.decode("utf-8")
    assert "id,date,activity_id" in csv_text
    assert "1,2025-05-03,1" in csv_text  

def test_export_all_registrations_to_csv(web_client, db_connection):
    db_connection.seed("Server/seeds/seed.sql")
    response = web_client.get("/registrations/export")
    assert response.status_code == 200
    assert response.mimetype == "text/csv"
    assert "attachment; filename=registrations.csv" in response.headers["Content-Disposition"]
    csv_text = response.data.decode("utf-8")
    assert "id,attendee_id,date_id" in csv_text
    assert "1,1,1" in csv_text  
