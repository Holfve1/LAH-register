from flask import Response
import csv
from io import StringIO
from lib.database_connection import get_flask_database_connection
from lib.repositories.activity_repo import ActivityRepository
from lib.repositories.attendee_repo import AttendeeRepository
from lib.repositories.date_repo import DateRepository
from lib.repositories.registration_repo import RegistrationRepository

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
    
