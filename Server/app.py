import os
from flask import Flask, request, render_template, flash
from lib.database_connection import get_flask_database_connection





# Create a new Flask app
app = Flask(__name__)
app.secret_key = 'i_dont_get_this'



if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
