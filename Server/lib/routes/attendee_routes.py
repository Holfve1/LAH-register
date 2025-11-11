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
    
    @app.route('/attendees', methods=['POST'])
    def create_attendee():
        connection = get_flask_database_connection(app)
        attendee_repo = AttendeeRepository(connection)
        data = request.get_json()
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        suburb = data.get('suburb')
        # Build an Attendee model and persist via the repository
        new_attendee = Attendee(None, first_name, last_name, suburb)
        attendee_repo.create(new_attendee)
        return jsonify({
            'message': 'Attendee created successfully',
            'attendee': {
                'id': new_attendee.id,
                'first_name': new_attendee.first_name,
                'last_name': new_attendee.last_name,
                'suburb': new_attendee.suburb
            }
        }), 201
    
    @app.route('/attendees/<int:id>', methods=['DELETE'])
    def delete_attendee(id):
        connection = get_flask_database_connection(app)
        attendee_repo = AttendeeRepository(connection)
        attendee_repo.delete(id)
        return '', 204 
    
    @app.route('/attendees/<int:id>', methods=['PATCH'])
    def update_attendee(id):
        connection = get_flask_database_connection(app)
        attendee_repo = AttendeeRepository(connection)
        data = request.get_json()
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        suburb = data.get('suburb')
        updated_attendee = attendee_repo.update(id, first_name, last_name, suburb)
        return jsonify({
            'message': 'Attendee updated successfully',
            'attendee': {
                'id': id,
                'first_name': first_name,
                'last_name': last_name,
                'suburb': suburb
            }
        }), 200