from flask import Response
import csv
from io import StringIO
from lib.database_connection import get_flask_database_connection
from lib.repositories.activity_repo import ActivityRepository

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
