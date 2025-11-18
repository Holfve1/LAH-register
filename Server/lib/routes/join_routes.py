from flask import Flask, jsonify, request
from lib.database_connection import get_flask_database_connection
from lib.repositories.join_repo import JoinRepository

def apply_join_routes(app):

    @app.route('/activities-by-attendee', methods=['GET'])
    def get_all_activities_by_attendee_id():
        connection = get_flask_database_connection(app)
        join_repo = JoinRepository(connection)
        attendee_id = request.args.get('id')
        rows = join_repo.find_activities_by_attendee_id(attendee_id)
        result = []
        for row in rows:
            result.append({
                'activity': row['activity'],
                'date': row['date']
            })
        return jsonify(result)
    
    @app.route('/attendees-and-activities', methods=['GET'])
    def get_all_attendees_and_their_activities():
        connection = get_flask_database_connection(app)
        join_repo = JoinRepository(connection)
        rows = join_repo.all_attendees_with_activities()
        result = []
        for row in rows:
            result.append({
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'activity': row['activity'],
            })
        return jsonify(result)
    
    @app.route('/dates-and-attendees-by-activity', methods=['GET'])
    def get_dates_and_attendees_by_activity_id():
        connection = get_flask_database_connection(app)
        join_repo = JoinRepository(connection)
        activity_id = request.args.get('id')
        rows = join_repo.find_dates_and_attendees_by_activity_id(activity_id)
        result = []
        for row in rows:
            result.append({
                'date': row['date'],
                'first_name': row['first_name'],
                'last_name': row['last_name']
            })
        return jsonify(result)
    
    @app.route('/activities-with-dates-and-attendees', methods=['GET'])
    def get_all_activities_with_dates_and_attendees():
        connection = get_flask_database_connection(app)
        join_repo = JoinRepository(connection)
        rows = join_repo.all_activities_with_dates_and_attendees()
        result = []
        for row in rows:
            result.append({
                'date': row['date'],
                'activity': row['activity'],
                'first_name': row['first_name'],
                'last_name': row['last_name']
            })
        return jsonify(result)

    @app.route('/date-with-activities-and-attendees', methods=['GET'])
    def get_a_date_with_activities_and_attendees():
        connection = get_flask_database_connection(app)
        join_repo = JoinRepository(connection)
        date_id = request.args.get('id')
        rows = join_repo.find_date_with_activities_and_attendees(date_id)
        result = []
        for row in rows:
            result.append({
                'date': row['date'],
                'activity': row['activity'],
                'first_name': row['first_name'],
                'last_name': row['last_name']
            })
        return jsonify(result)
    
    @app.route('/all-dates-with-activities-and-attendees', methods=['GET'])
    def get_all_dates_with_activities_and_attendees():
        connection = get_flask_database_connection(app)
        join_repo = JoinRepository(connection)
        rows = join_repo.all_dates_with_activities_and_attendees()
        result = []
        for row in rows:
            result.append({
                'date': row['date'],
                'activity': row['activity'],
                'first_name': row['first_name'],
                'last_name': row['last_name']
            })
        return jsonify(result)



        