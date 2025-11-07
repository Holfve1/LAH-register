from flask import Flask, jsonify
from lib.database_connection import get_flask_database_connection
from lib.repositories.attendee_repo import AttendeeRepository

def apply_attendee_routes(app):

    @app.route('/attendees', methods=['GET'])
    def get_all_attendees():
        connection = get_flask_database_connection(app)
        attendee_repo = AttendeeRepository(connection)
        attendees = attendee_repo.all()
        result = []
        for attendee in attendees:
            result.append({
                "id": attendee.id,
                "first_name": attendee.first_name,
                "last_name": attendee.last_name,
                "suburb": attendee.suburb
            })
        return jsonify(result)  