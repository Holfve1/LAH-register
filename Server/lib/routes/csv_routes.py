from flask import Response, request
import csv
from io import StringIO
from lib.database_connection import get_flask_database_connection
from lib.repositories.activity_repo import ActivityRepository
from lib.repositories.attendee_repo import AttendeeRepository
from lib.repositories.date_repo import DateRepository
from lib.repositories.registration_repo import RegistrationRepository
from lib.repositories.join_repo import JoinRepository

def apply_csv_routes(app):

    @app.route('/activities/export', methods=['GET'])
    def export_all_activities_to_csv():     
        connection = get_flask_database_connection(app)
        activity_repo = ActivityRepository(connection)
        activities = activity_repo.all()
        buffer = StringIO() 
        writer = csv.writer(buffer)
        writer.writerow(['id', 'activity'])
        for a in activities:
            writer.writerow([a.id, a.activity])
        csv_data = buffer.getvalue()
        buffer.close()
        return Response(
            csv_data,
            mimetype='text/csv',
            headers={'Content-Disposition': 'attachment; filename=activities.csv'}
        )
    
    @app.route('/attendees/export', methods=['GET'])
    def export_all_attendees_to_csv():     
        connection = get_flask_database_connection(app)
        attendee_repo = AttendeeRepository(connection)
        attendees = attendee_repo.all()
        buffer = StringIO() 
        writer = csv.writer(buffer)
        writer.writerow(['id', 'first_name', 'last_name', 'suburb'])
        for a in attendees:
            writer.writerow([a.id, a.first_name, a.last_name, a.suburb])
        csv_data = buffer.getvalue()
        buffer.close()
        return Response(
            csv_data,
            mimetype='text/csv',
            headers={'Content-Disposition': 'attachment; filename=attendees.csv'}
        )
    
    @app.route('/dates/export', methods=['GET'])
    def export_all_dates_to_csv():     
        connection = get_flask_database_connection(app)
        date_repo = DateRepository(connection)
        dates = date_repo.all()
        buffer = StringIO() 
        writer = csv.writer(buffer)
        writer.writerow(['id', 'date', 'activity_id'])
        for d in dates:
            writer.writerow([d.id, d.date, d.activity_id])
        csv_data = buffer.getvalue()
        buffer.close()
        return Response(
            csv_data,
            mimetype='text/csv',
            headers={'Content-Disposition': 'attachment; filename=dates.csv'}
        )
    
    @app.route('/registrations/export', methods=['GET'])
    def export_all_registrations_to_csv():     
        connection = get_flask_database_connection(app)
        registration_repo = RegistrationRepository(connection)
        registrations = registration_repo.all()
        buffer = StringIO() 
        writer = csv.writer(buffer)
        writer.writerow(['id', 'attendee_id', 'date_id'])
        for r in registrations:
            writer.writerow([r.id, r.attendee_id, r.date_id])
        csv_data = buffer.getvalue()
        buffer.close()
        return Response(
            csv_data,
            mimetype='text/csv',
            headers={'Content-Disposition': 'attachment; filename=registrations.csv'}
        )
    
    @app.route('/attendee-activities/export', methods=['GET'])
    def export_attendee_activities_to_csv():
        connection = get_flask_database_connection(app)
        join_repo = JoinRepository(connection)
        attendee_id = request.args.get('id')
        rows = join_repo.find_activities_by_attendee_id(attendee_id)
        buffer = StringIO() 
        writer = csv.writer(buffer)
        writer.writerow(['activity', 'date'])
        for row in rows:
            writer.writerow([row['activity'], row['date']])
        csv_data = buffer.getvalue()
        buffer.close()
        return Response(
            csv_data,
            mimetype='text/csv',
            headers={'Content-Disposition': 'attachment; filename=attendee_activities.csv'}
        )

    @app.route('/activities-attendees/export', methods=['GET'])
    def export_activities_and_attendees_to_csv():
        connection = get_flask_database_connection(app)
        join_repo = JoinRepository(connection)
        rows = join_repo.all_attendees_with_activities()
        buffer = StringIO() 
        writer = csv.writer(buffer)
        writer.writerow(['activity', 'first_name', 'last_name'])
        for row in rows:
            writer.writerow([row['activity'], row['first_name'], row['last_name']])
        csv_data = buffer.getvalue()
        buffer.close()
        return Response(
            csv_data,
            mimetype='text/csv',
            headers={'Content-Disposition': 'attachment; filename=activities_attendees.csv'}
        )

    @app.route('/activity-dates-attendees/export', methods=['GET'])
    def export_activity_dates_attendees_to_csv():
        connection = get_flask_database_connection(app)
        join_repo = JoinRepository(connection)
        activity_id = request.args.get('id')
        rows = join_repo.find_dates_and_attendees_by_activity_id(activity_id)
        buffer = StringIO()
        writer = csv.writer(buffer)
        writer.writerow(['date', 'first_name', 'last_name'])
        for row in rows:
            writer.writerow([row['date'], row['first_name'], row['last_name']])
        csv_data = buffer.getvalue()
        buffer.close()
        return Response(
            csv_data,
            mimetype = 'text/csv',
            headers={'Content-Disposition': 'attachment; filename=activity-dates-attendees.csv'}
        )

    @app.route('/activities-dates-attendees/export', methods=['GET'])
    def export_activities_dates_attendees_to_csv():
        connection = get_flask_database_connection(app)
        join_repo = JoinRepository(connection)
        rows = join_repo.all_activities_with_dates_and_attendees()
        buffer = StringIO()
        writer = csv.writer(buffer)
        writer.writerow(['date', 'activity', 'first_name', 'last_name'])
        for row in rows:
            writer.writerow([row['date'], row['activity'], row['first_name'], row['last_name']])
        csv_data = buffer.getvalue()
        buffer.close()
        return Response(
            csv_data,
            mimetype='text/csv',
            headers={'Content-Disposition': 'attachment; filename=activities-dates-attendees.csv'}
        )

    @app.route('/date-activities-attendees/export', methods=['GET'])
    def export_date_activities_attendees_to_csv():
        connection = get_flask_database_connection(app)
        join_repo = JoinRepository(connection)
        date_id = request.args.get('id')
        rows = join_repo.find_date_with_activities_and_attendees(date_id)
        buffer = StringIO()
        writer = csv.writer(buffer)
        writer.writerow(['date', 'activity', 'first_name', 'last_name'])
        for row in rows:
            writer.writerow([row['date'], row['activity'], row['first_name'], row['last_name']])
        csv_data = buffer.getvalue()
        buffer.close()
        return Response(
            csv_data,
            mimetype='text/csv',
            headers={'Content-Disposition': 'attachment; filename=date-activities-attendees.csv'}
        )

    @app.route('/dates-activities-attendees/export', methods=['GET'])
    def export_dates_activities_attendees_to_csv():
        connection = get_flask_database_connection(app)
        join_repo = JoinRepository(connection)
        rows = join_repo.all_dates_with_activities_and_attendees()
        buffer = StringIO()
        writer = csv.writer(buffer)
        writer.writerow(['date', 'activity', 'first_name', 'last_name'])
        for row in rows:
            writer.writerow([row['date'], row['activity'], row['first_name'], row['last_name']])
        csv_data = buffer.getvalue()
        buffer.close()
        return Response(
            csv_data,
            mimetype='text/csv',
            headers={'Content-Disposition': 'attachment; filename=dates-activities-attendees.csv'}
        )



