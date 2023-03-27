"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app
from flask import abort, render_template, request, jsonify, send_file, send_from_directory
import os
from app.models import *
from werkzeug.utils import secure_filename
from app.Scripts.tts import *

phrases = []

###
# Routing for your application.
###


@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")


###
# The functions below should be applicable to all Flask apps.
###


# Profile Section
# @app.route('api/profile')
# @app.route('api/profile/adduser')
# @app.route('api//profile/adduser2')
# @app.route('api//profile/adduser3')
# @app.route('api//profile/adduser4')
# @app.route('api//profile/adduser5')

# Speaking Screen
@app.route('/api/speak', methods=['POST'])
def speak():
    if request.method == 'POST':
        text = request.form['speech']
        gender = request.form['voices']
        # rate = request.form['speed']
        text_to_speech(text, gender)
        return 200
    
#Listening Screen


# Saved Phrases


# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            )
            error_messages.append(message)

    return error_messages


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return jsonify(error="Page Not Found"), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
