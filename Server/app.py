import os
from flask import Flask, jsonify, request, render_template, flash
from flask_cors import CORS
from lib.routes.join_routes import apply_join_routes
from lib.database_connection import get_flask_database_connection
from lib.routes.attendee_routes import apply_attendee_routes
from lib.routes.activity_routes import apply_activity_routes
from lib.routes.csv_routes import apply_csv_routes
from lib.routes.date_routes import apply_date_routes
from lib.routes.registration_routes import apply_registration_routes
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
load_dotenv()

# Create a new Flask app
app = Flask(__name__)
app.secret_key = 'i_dont_get_this'
CORS(app, origins=["http://localhost:5173"]) #need to change for/update for deployment

apply_attendee_routes(app)
apply_activity_routes(app)
apply_date_routes(app)
apply_registration_routes(app)
apply_join_routes(app)

apply_csv_routes(app)

ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
SEND_TO_EMAIL = os.getenv("SEND_TO_EMAIL")
SMTP_EMAIL = os.getenv("SMTP_EMAIL")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    entered_password = data.get('password')

    # Load from environment variable
    admin_password = os.getenv('ADMIN_PASSWORD')

    if entered_password == admin_password:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False}), 401



@app.post("/forgot-password")
def forgot_password():
    try:
        msg = EmailMessage()
        msg["Subject"] = "Admin Password Reminder"
        msg["From"] = SMTP_EMAIL
        msg["To"] = SEND_TO_EMAIL
        msg.set_content(f"The admin password is: {ADMIN_PASSWORD}")

       
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(SMTP_EMAIL, SMTP_PASSWORD)
            smtp.send_message(msg)

        return jsonify({"success": True})

    except Exception as e:
        print("Email sending failed:", e)
        return jsonify({"success": False, "error": str(e)})



if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))