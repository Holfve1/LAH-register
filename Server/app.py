import os
from flask import Flask, request, render_template, flash
from lib.routes.join_routes import apply_join_routes
from lib.database_connection import get_flask_database_connection
from lib.routes.attendee_routes import apply_attendee_routes
from lib.routes.activity_routes import apply_activity_routes
from lib.routes.csv_routes import apply_csv_routes
from lib.routes.date_routes import apply_date_routes
from lib.routes.registration_routes import apply_registration_routes

# Create a new Flask app
app = Flask(__name__)
app.secret_key = 'i_dont_get_this'


apply_attendee_routes(app)
apply_activity_routes(app)
apply_date_routes(app)
apply_registration_routes(app)
apply_join_routes(app)

apply_csv_routes(app)


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
