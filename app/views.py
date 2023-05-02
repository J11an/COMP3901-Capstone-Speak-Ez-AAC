"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app,socketio
from flask import abort, render_template, request, jsonify, send_file, send_from_directory
import os
from app.models import *
from werkzeug.utils import secure_filename
from app.Scripts.tts import *
from app.Scripts.vosk_speech_rec import *
from vosk import Model, KaldiRecognizer
import pandas as pd



phrases = []
rootdir = os.getcwd()
model_dir = (os.path.join(rootdir + r"\model\vosk-model-small-en-us-0.15"))
model = Model(model_dir)
rec = KaldiRecognizer(model, 16000)


###
# Routing for your application.
###g


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
        mp3 = os.path.join(rootdir,r"message.mp3")
        return send_file(mp3, mimetype='audio/mp3', as_attachment=True)
 

@app.route('/',methods=["GET"])    
def word_associated():
# takes a word and returns a list of next parts of speech and the associated
# list of words for each


    tile=Tile.query.filter_by(word=Tile.word).first()
    if tile is None:
        return jsonify({'error':'Word not found.'}),404

    next_partsofspeech={
        'noun':[],
        'verb':[],
        'adjective':[],
        'article':[]
    }

    if tile.partofspeech=='noun':
        next_partsofspeech['adjective']=[t.word for t in Tile.query.filter_by(partofspeech='adjective').all()]
        next_partsofspeech['verb']=[t.word for t in Tile.query.filter_by(partofspeech='verb').all()]

    elif tile.partofspeech=='verb':
        next_partsofspeech['noun']=[t.word for t in Tile.query.filter_by(partofspeech='noun').all()]
        
    if tile.partofspeech=='adjective':
        next_partsofspeech['noun']=[t.word for t in Tile.query.filter_by(partofspeech='noun').all()]
        



    return jsonify(next_partsofspeech)
   
@app.route('/inital_tree_setting')     
def inital_tree_setting():
    columns={
        "noun":[],
        "verb":[],
        "adjective":[],
        "article":[]
    }       
    #Retieve all the title from the database and group them by theier part of speech
    tiles=Tile.query.all()
    for tile in tiles:
        part_of_speech=tile.partofspeech.lower()
        if part_of_speech in columns:
            columns[part_of_speech].append(tile.word)
    # Fill in any missing words up to maximum of 4 per part of speech
    for coluumn in columns.values():
        while len(coluumn)<4:
            coluumn.append ("")

    return jsonify(columns)
    
    
#Listening Screen
@app.route('/api/listen',methods=['POST'])
def listen():
    if request.method == 'POST':
        data = request.data
        rec.AcceptWaveform(data)
        result = rec.Result()
        result_json = jsonify({"text": result})
        return result_json


# Saved Phrases


#Seed Vocab List
@app.route('/seed_database')
def seed_database():

    df = pd.read_excel('vocab_list.xlsx', sheet_name=None)

    for sheet_name, sheet_data in df.items():
        for index, row in sheet_data.iterrows():
            tile = Tile(

                word = ['word'],
                partofspeech = ['partofspeech'],
                category = ['category'],
                time = ['time'],
                place = ['place'],
                plural = ['plural'],
                photo = ['photo']
            )
            db.session.add(tile)
            db.session.commit()

    return "Database seeded successfully"

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
