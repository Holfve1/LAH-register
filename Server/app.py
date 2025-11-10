import os
from flask import Flask, request, render_template, flash
from lib.database_connection import get_flask_database_connection
from lib.routes.attendee_routes import apply_attendee_routes
from lib.routes.activity_routes import apply_activity_routes


# Create a new Flask app
app = Flask(__name__)
app.secret_key = 'i_dont_get_this'


apply_attendee_routes(app)
apply_activity_routes(app)


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
