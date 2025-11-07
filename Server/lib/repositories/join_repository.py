from lib.models.attendee import Attendee
from lib.models.activity import Activity
from lib.models.date import Date
from lib.models.registration import Registration
class JoinRepository:
    def __init__(self, connection):
        self.connection = connection
# Attendee related queries
# Returns a list of activities for a given attendee_id
    def find_activities_by_attendee_id(self, attendee_id):
        query = '''
            SELECT a.activity, d.date
            FROM registrations r
            JOIN dates d ON r.date_id = d.id
            JOIN activities a ON d.activity_id = a.id
            WHERE r.attendee_id = %s
            ORDER BY d.date;
        '''
        rows = self.connection.execute(query, [attendee_id])
        return rows
# “Show me the activity name and the date for every registration where the registration belongs to a specific attendee (attendee_id = %s). Sort the results by date.”
# Returns a list of all attendees with their activities
    def all_attendees_with_activities(self):
        #DISTINCT gets rid of duplicates combinations between columns
        query = '''
            SELECT DISTINCT a.activity, at.first_name, at.last_name
            FROM registrations r
            JOIN attendees at ON r.attendee_id = at.id
            JOIN dates d ON r.date_id = d.id
            JOIN activities a ON d.activity_id = a.id
            ORDER by a.id, at.last_name, at.first_name;
        '''
        rows = self.connection.execute(query)
        return rows
# Activity related queries
# Returns a list of dates and attendees for a given activity_id
    def find_dates_and_attendees_by_activity_id(self, activity_id):
        query = '''
            SELECT d.date, at.first_name, at.last_name
            FROM registrations r
            JOIN attendees at ON r.attendee_id = at.id
            JOIN dates d ON r.date_id = d.id
            JOIN activities a ON d.activity_id = a.id
            WHERE a.id = %s
            ORDER by d.date;
        '''
        rows = self.connection.execute(query, [activity_id])
        return rows
# Returns a list of all activities with their dates and attendees
    def all_activities_with_dates_and_attendees(self):
        query = '''
            SELECT d.date, a.activity, at.first_name, at.last_name
            FROM registrations r
            JOIN attendees at ON r.attendee_id = at.id
            JOIN dates d ON r.date_id = d.id
            JOIN activities a ON d.activity_id = a.id
            ORDER by a.id, d.date, at.last_name, at.first_name;
        '''
        rows = self.connection.execute(query)
        return rows
# Date related queries
# Returns a date with its activities and attendees
    def find_date_with_activities_and_attendees(self, date_id):
        query = '''
            SELECT d.date, a.activity, at.first_name, at.last_name
            FROM registrations r
            JOIN dates d ON r.date_id = d.id
            JOIN activities a ON d.activity_id = a.id
            JOIN attendees at ON r.attendee_id = at.id
            WHERE d.id = %s
            ORDER BY a.activity, at.last_name, at.first_name;
            '''
        rows = self.connection.execute(query, [date_id])
        return rows
# Returns a list of all dates with their activities and attendees
    def all_dates_with_activities_and_attendees(self):
        query = '''
            SELECT d.date, a.activity, at.first_name, at.last_name
            FROM registrations r
            JOIN dates d ON r.date_id = d.id
            JOIN activities a ON d.activity_id = a.id
            JOIN attendees at ON r.attendee_id = at.id
            ORDER BY d.date, a.activity, at.last_name, at.first_name;
            '''
        rows = self.connection.execute(query)
        return rows