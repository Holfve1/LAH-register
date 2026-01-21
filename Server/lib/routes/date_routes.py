from flask import Flask, jsonify, request
from lib.database_connection import get_flask_database_connection
from lib.repositories.date_repo import DateRepository
from lib.models.date import Date

def apply_date_routes(app):
    

    @app.route('/dates', methods=['GET'])
    def get_all_dates():
        connection = get_flask_database_connection(app)        
        date_repo = DateRepository(connection)
        dates = date_repo.all()
        result = []
        for date in dates:
            result.append({
                'id': date.id,
                'date': str(date.date),
                'activity_id': date.activity_id
            })
        return jsonify(result)

    @app.route('/dates', methods=['POST'])
    def create_new_date():
        connection = get_flask_database_connection(app)
        date_repo = DateRepository(connection)
        data = request.get_json()

        date_value = data.get('date')
        activity_id = data.get('activity_id')

        existing = date_repo.find_by_date_and_activity_id(date_value, activity_id)
        if existing:
            return jsonify({
                'message': 'Date already exists',
                'id': existing.id,
                'date': str(existing.date),
                'activity_id': existing.activity_id
            }), 200

        new_date = Date(None, date_value, activity_id)
        date_repo.create(new_date)

        return jsonify({
            'message': 'Date created successfully',
            'id': new_date.id,
            'date': str(new_date.date),
            'activity_id': new_date.activity_id
        }), 201
    
    @app.route('/dates/<int:id>', methods=['DELETE'])
    def delete_date(id):
        connection = get_flask_database_connection(app)
        date_repo = DateRepository(connection)
        date_repo.delete(id)
        return '', 204
    
    @app.route('/dates/<int:id>', methods=['PATCH'])
    def update_date(id):
        connection = get_flask_database_connection(app)
        date_repo = DateRepository(connection)
        data = request.get_json()
        date = data.get('date')
        activity_id = data.get('activity_id')
        updated_date = date_repo.update(id, date, activity_id)
        return jsonify({
            'message': 'Date updated successfully',
            'id': id,
            'date': str(date),
            'activity_id': activity_id
            }),  200