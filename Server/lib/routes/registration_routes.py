from flask import Flask, jsonify, request
from lib.database_connection import get_flask_database_connection
from lib.repositories.registration_repo import RegistrationRepository
from lib.models.registration import Registration


def apply_registration_routes(app):
    

    @app.route('/registrations', methods=['GET'])
    def get_all_registrations():
        connection = get_flask_database_connection(app)        
        registration_repo = RegistrationRepository(connection)
        registrations = registration_repo.all()
        result = []
        for registration in registrations:
            result.append({
                'id': registration.id,
                'attendee_id': registration.attendee_id,
                'date_id': registration.date_id,
            })
        return jsonify(result)
    
    @app.route('/registrations', methods=['POST'])
    def create_registration():
        connection = get_flask_database_connection(app)
        registration_repo = RegistrationRepository(connection)
        data = request.get_json()
        date_id = data.get('date_id')
        attendee_id = data.get('attendee_id')
        new_registration = Registration(None, attendee_id, date_id)
        registration_repo.create(new_registration)
        return jsonify({
            'message': 'Registration created successfully',
            'registration': {
                'id': new_registration.id,
                'attendee_id': new_registration.attendee_id,
                'date_id': new_registration.date_id
            }
        }), 201
    
    @app.route('/registrations/<int:id>', methods=['DELETE'])
    def delete_registration(id):
        connection = get_flask_database_connection(app)
        registration_repo = RegistrationRepository(connection)
        registration_repo.delete(id)
        return '', 204 
    
    @app.route('/registrations/<int:id>', methods=['PATCH'])
    def update_registration(id):
        connection = get_flask_database_connection(app)
        registration_repo = RegistrationRepository(connection)
        data = request.get_json()
        date_id = data.get('date_id')
        attendee_id = data.get('attendee_id')
        registration_repo.update(id, attendee_id, date_id)
        return jsonify({
            'message': 'Registration updated successfully',}
        ), 200