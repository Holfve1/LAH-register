from flask import Flask, jsonify, request
from lib.database_connection import get_flask_database_connection
from lib.repositories.activity_repo import ActivityRepository
from lib.models.activity import Activity

def apply_activity_routes(app):

    @app.route('/activities', methods=['GET'])
    def get_all_activities():
        connection = get_flask_database_connection(app)
        activity_repo = ActivityRepository(connection)
        activities = activity_repo.all()
        result = []
        for activity in activities:
            result.append({
                "id": activity.id,
                "activity": activity.activity
               
            })
        return jsonify(result)  
    
    @app.route('/activities', methods=['POST'])
    def create_activity():
        connection = get_flask_database_connection(app)
        activity_repo = ActivityRepository(connection)
        data = request.get_json()
        activity_name = data.get('activity')
        # Build an Activity model and persist via the repository
        new_activity = Activity(None, activity_name)
        activity_repo.create(new_activity)
        return jsonify({
            'message': 'Activity created successfully',
            'activity': {
                'id': new_activity.id,
                'activity': new_activity.activity
            }
        }), 201

    @app.route('/activities/<int:id>', methods=['DELETE'])
    def delete_activity(id):
        connection = get_flask_database_connection(app)
        activity_repo = ActivityRepository(connection)
        activity_repo.delete(id)
        return '', 204

    @app.route('/activities/<int:id>', methods=['PATCH'])
    def update_activity():
        connection = get_flask_database_connection(app)
        activity_repo = ActivityRepository(connection)
        data = request.get_json()
        activity_name = data.get('activity')
        updated_activity = activity_repo.update(id, activity_name)
        return jsonify({
            'message': 'Activity created updated',
            'activity': {
                'id': id,
                'activity': updated_activity.activity
            }
        }), 200
