#!/usr/bin/python3
"""
ussd_app.py
------------
Africa's Talking SSD (USSD) example using Flask.

Modules:
    - africastalking: Africa's Talking official Python SDK.
    - flask: lightweight web framework to handle USSD callbacks.

Linux setup:
    pip install africastalking flask

Run locally:
    python3 ussd_app.py

Use ngrok or your server public IP to expose the port 5000 to Africa's Talking sandbox.
"""

from flask import Flask, request
import africastalking

# Initialize Flask app
app = Flask(__name__)

# Initialize Africa's Talking credentials
USERNAME = "sandbox"  # Use 'sandbox' for testing
API_KEY = "YOUR_API_KEY_HERE"  # Get it from https://account.africastalking.com

africastalking.initialize(USERNAME, API_KEY)

@app.route('/ussd', methods=['POST'])
def ussd_callback():
    """
    Handle Africa's Talking USSD requests and respond with next menu.
    """
    session_id = request.form.get('sessionId')
    service_code = request.form.get('serviceCode')
    phone_number = request.form.get('phoneNumber')
    text = request.form.get('text')

    # Split user input
    user_response = text.split("*") if text else []

    # USSD menu logic
    if text == "":
        # main menu
        response = "CON Welcome to Ressen Tech USSD\n"
        response += "1. Register\n"
        response += "2. Check Balance\n"
        response += "3. Exit"
    elif text == "1":
        response = "CON Enter your full name:"
    elif len(user_response) == 2 and user_response[0] == "1":
        name = user_response[1]
        response = f"END Thanks {name}, you have been registered successfully!"
    elif text == "2":
        # This could fetch from database later
        response = "END Your account balance is KES 500"
    elif text == "3":
        response = "END Goodbye!"
    else:
        response = "END Invalid choice"

    return response, 200, {"Content-Type": "text/plain"}

if __name__ == '__main__':
    # Flask runs on port 5000 by default
    app.run(host='0.0.0.0', port=5000, debug=True)

