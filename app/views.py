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
import random
from sqlalchemy import func
from difflib import get_close_matches


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
 
@app.route('/api/word_associated',methods=['POST','GET'])    
def word_associated():
    next_partsofspeech={}
    # tile=Words.query.filter_by(word_id=Words.word_id).first()

    next_partsofspeech["adjectives"] = [{"id": adjectives.word_id, "word": adjectives.word, "symbol": Symbols.query.filter_by(symbol_id=adjectives.symbol_id).first()} for adjectives in Words.query.filter_by(partofspeech='Adjectives', word="red").order_by(func.random()).limit(4).all()]

    # if tile.partofspeech=='Noun':
    #     next_partsofspeech["adjectives"] = [adjective.word for adjective in Words.query.filter_by(partofspeech='Adjectives').order_by(func.random()).limit(4).all()]
    #     next_partsofspeech["preposition"] = [preposition.word for preposition in Words.query.filter_by(partofspeech='Preposition').order_by(func.random()).limit(4).all()]
        # next_partsofspeech["conjunction"] = [{"id": conjunction.word_id, "word": conjunction.word, "symbol": Symbols.query.filter_by(symbol_id=conjunction.symbol_id).first()} for conjunction in Words.query.filter_by(partofspeech='Conjunction').order_by(func.random()).limit(4).all()]
    #     next_partsofspeech["verb"] = [verb.word for verb in Words.query.filter_by(partofspeech='Verb').order_by(func.random()).limit(4).all()]
    #     next_partsofspeech["noun"] = [noun.word for noun in Words.query.filter_by(partofspeech='Noun').order_by(func.random()).limit(4).all()]

    # if tile.partofspeech=='Article':
    #     next_partsofspeech["adjectives"] = [adjective.word for adjective in Words.query.filter_by(partofspeech='Adjectives').order_by(func.random()).limit(4).all()]
    #     next_partsofspeech["noun"] = [noun.word for noun in Words.query.filter_by(partofspeech='Noun').order_by(func.random()).limit(4).all()]

    # if tile.partofspeech=='Pronoun':

    #     next_partsofspeech["preposition"] = [preposition.word for preposition in Words.query.filter_by(partofspeech='Preposition').order_by(func.random()).limit(4).all()]
    #     next_partsofspeech["verb"] = [verb.word for verb in Words.query.filter_by(partofspeech='Verb').order_by(func.random()).limit(4).all()]
    #     next_partsofspeech["noun"] = [noun.word for noun in Words.query.filter_by(partofspeech='Noun').order_by(func.random()).limit(4).all()]

    # if tile.partofspeech=='Preposition':
    #     next_partsofspeech["articles"] = [articles.word for articles in Words.query.filter_by(partofspeech='Articles').order_by(func.random()).limit(4).all()]
    #     next_partsofspeech["noun"] = [noun.word for noun in Words.query.filter_by(partofspeech='Noun').order_by(func.random()).limit(4).all()]
    #     next_partsofspeech["pronoun"] = [pronoun.word for pronoun in Words.query.filter_by(partofspeech='Pronoun').order_by(func.random()).limit(4).all()]

    # if tile.partofspeech=='Conjunction':
    #     next_partsofspeech["verb"] = [verb.word for verb in Words.query.filter_by(partofspeech='Verb').order_by(func.random()).limit(4).all()]
    #     next_partsofspeech["articles"] = [articles.word for articles in Words.query.filter_by(partofspeech='Articles').order_by(func.random()).limit(4).all()]
    #     next_partsofspeech["pronoun"] = [pronoun.word for pronoun in Words.query.filter_by(partofspeech='Pronoun').order_by(func.random()).limit(4).all()]

    # if tile.partofspeech=='Adjectives':
    #     next_partsofspeech["adjectives"] = [adjective.word for adjective in Words.query.filter_by(partofspeech='Adjectives').order_by(func.random()).limit(4).all()]
    #     next_partsofspeech["conjunction"] = [conjunction.word for conjunction in Words.query.filter_by(partofspeech='Conjunction').order_by(func.random()).limit(4).all()]
    #     next_partsofspeech["noun"] = [noun.word for noun in Words.query.filter_by(partofspeech='Noun').order_by(func.random()).limit(4).all()]

    # if tile.partofspeech=='Verb':
    #     next_partsofspeech["adjectives"] = [adjective.word for adjective in Words.query.filter_by(partofspeech='Adjectives').order_by(func.random()).limit(4).all()]
    #     next_partsofspeech["preposition"] = [preposition.word for preposition in Words.query.filter_by(partofspeech='Preposition').order_by(func.random()).limit(4).all()]
    #     next_partsofspeech["articles"] = [articles.word for articles in Words.query.filter_by(partofspeech='Articles').order_by(func.random()).limit(4).all()]
    #     next_partsofspeech["verb"] = [verb.word for verb in Words.query.filter_by(partofspeech='Verb').order_by(func.random()).limit(4).all()]
    #     next_partsofspeech["noun"] = [noun.word for noun in Words.query.filter_by(partofspeech='Noun').order_by(func.random()).limit(4).all()]
    #     next_partsofspeech["pronoun"] = [pronoun.word for pronoun in Words.query.filter_by(partofspeech='Pronoun').order_by(func.random()).limit(4).all()]

    return jsonify(next_partsofspeech),200


@app.route('/api/search/<word>',methods=['POST'])
def search_word(word):
    if request.method == 'POST':
        search_result = Words.query.filter(Words.word.ilike(f'%{word}%')).all()
        #n specifies the maximum number of closest matches to return and 
        # cutoff is specifies a threshold for how closely a word needs to match the input word to be considered a match between 0 and 1
        matches = get_close_matches(word, [w.word for w in search_result], n=10, cutoff=0.6)
        return (jsonify(matches))
            




# @app.route('/api/word_associated',methods=['POST'])    
# def word_associated(word):
# # takes a word and returns a list of next parts of speech and the associated
# # list of words for each
#     if request.method == "POST":



#     tile=Words.query.filter_by(word=Words.word).first()
#     print(tile)
#     if tile is None:
#         return jsonify({'error':'Word not found.'}),404

#     next_partsofspeech={
#         'noun':[],
#         'verb':[],
#         'adjective':[],
#         'article':[],
#         'pronoun':[]
#     }

#     if tile.partofspeech=='noun':
#         next_partsofspeech['adjective']=[t.word for t in Words.query.filter_by(partofspeech='Adjectives').all()]
#         next_partsofspeech['verb']=[t.word for t in Words.query.filter_by(partofspeech='verb').all()]

#     elif tile.partofspeech=='verb':
#         next_partsofspeech['noun']=[t.word for t in Words.query.filter_by(partofspeech='noun').all()]
        
#     elif tile.partofspeech=='adjective':
#         next_partsofspeech['noun']=[t.word for t in Words.query.filter_by(partofspeech='noun').all()]

#     elif tile.partofspeech=='pronoun':
#         next_partsofspeech['pronoun']=[t.word for t in Words.query.filter_by(partofspeech='pronoun').all()]
        
#     elif tile.partofspeech=='article':
#         next_partsofspeech['article']=[t.word for t in Words.query.filter_by(partofspeech='article').all()]
        

#     return jsonify(next_partsofspeech)


# @app.route('/',methods=['GET'])
# def get_categories():

#     categories=Words.query.filter_by(category=Words.category).first()
#     print(categories)
#     if categories is None:
#         return jsonify({'error':'Word not found'}),404

#     groups={
#         'Family':[],
#         'Colours':[],
#     }

   
@app.route('/api/inital_tree_setting',methods = ['GET'])    
def inital_tree_setting():
    columns={
        "noun":[],
        "verb":[],
        "adjectives":[],
        "articles":[],
        "pronoun":[]
    }       
    #Retrieve all the title from the database and group them by their part of speech
    tiles=Words.query.all()
    for tile in tiles:
        part_of_speech=tile.partofspeech.lower()
        print(part_of_speech)
        if part_of_speech in columns:
            columns[part_of_speech].append(tile.word)
        
    # columns[part_of_speech].append(tile.word_id)
            # columns[part_of_speech].append(tile.symbol_id)


            
    # Shuffle the words in each column and take the first 4
    for column in columns:  
        random.shuffle(columns[column])
        columns[column]=tuple(columns[column][:4])
    
    return jsonify(columns),201

@app.route('/api/get_categories',methods=['GET'])
def get_catergories():
    categories=db.session.query(Words.category).distinct().all()
    categories=[c[0] for c in categories]
    return jsonify(categories)

@app.route('/api/get_word_symbol',methods=['GET'])
def get_word_sybmol(): 
    word=request.args.get('word')
    word_obj=Words.query.filter_by(word=Words.word).first()
    if word_obj:
        symbol_id=word_obj.symbol_id
        symbol_obj=Symbols.query.get(symbol_id)
        symbol=symbol_obj.symbol
        result={
            'word':word_obj.word,
            'id': word_obj.word_id,
            'symbol':symbol
        }
        return jsonify(result)
    else:
        return jsonify({'error':'Word not found'})
    
    
#Listening Screen
@app.route('/api/listen',methods=['POST'])
def listen():
    if request.method == 'POST':
        data = request.data
        rec.AcceptWaveform(data)
        result = rec.Result()
        result_json = jsonify({"text": result})
        return result_json

@socketio.on('audio_data')
def handle_audio_data(data):
    print('received audio data:', data)
    socketio.emit('my_response', data)

    
# Saved Phrases


#Seed Vocab List
@app.route('/api/seed_database')
def seed_database():
    #Change file path to the one on your computer (Temp Maybe). Lol use os.path
    df = pd.read_excel(f"{os.path.abspath(os.getcwd())}\\app\\Vocab list.xlsx", sheet_name=None)

    for sheet_name, sheet_data in df.items():
        if sheet_name == "Words":
            for index, row in sheet_data.iterrows():
                cword = Words(
                word=(row['word']),
                partofspeech=(row['part_of_speech']),
                category=(row['category']),
                sub_category=(row['sub_category']),
                time=(row['time']),
                place=(row['place']),
                symbol_id=(row['symbol_id']),
                )
                db.session.add(cword)
                db.session.commit()
                
        if sheet_name == "Parts_of_speech":
            for index, row in sheet_data.iterrows():
                cpartofspeech=PartsofSpeech(
                pos_id=(row['pos_id']),
                pos=(row['pos'])
                )
                db.session.add(cpartofspeech)
                db.session.commit()
        if sheet_name == "Adjectives":
            for index, row in sheet_data.iterrows():
                cAdjectives= Adjectives(
                word_id=(row['word_id']),
                word=(row['word']),
                pos_id=(row['pos_id']),
                comparative=(row['comparative']),
                superlative=(row['superlative'])
                )
                db.session.add(cAdjectives)
                db.session.commit()
        if sheet_name == "Nouns":
            for index, row in sheet_data.iterrows():
                cNoun=Nouns(
                word_id=(row['word_id']),
                word=(row['word']),
                pos_id=(row['pos_id']),
                plural=(row['plural']),
                possessive=(row['possessive']),
                male=(row['male']),
                female=(row['Female'])            
                )
                db.session.add(cNoun)
                db.session.commit()
        if sheet_name == "Verbs":
            for index, row in sheet_data.iterrows():
                cVerb=Verbs(
                word_id=(row['word_id']),
                word=(row['word']),
                pos_id=(row['pos_id']),
                plural=(row['plural']),
                past=(row['past']),
                present_cont=(row['present_cont']),
                future=(row['future']),
                perfect=(row['perfect'])               
                )
                db.session.add(cVerb)
                db.session.commit()
        if sheet_name == "Symbols":
            for index, row in sheet_data.iterrows():
                cSymbol=Symbols(
                symbol_id=(row['symbol_id']),
                symbol=(row['symbol'])
                )
                db.session.add(cSymbol)
                db.session.commit()
        if sheet_name == "Pronouns":
            for index, row in sheet_data.iterrows():
                cPronoun=Pronouns(
                word_id=(row['word_id']),
                word=(row['word'])
                )
                db.session.add(cPronoun)
                db.session.commit()
        if sheet_name == "Articles":
            for index, row in sheet_data.iterrows():
                cArticle=Articles(
                word_id=(row['word_id']),
                word=(row['word'])
                )
                db.session.add(cArticle)
                db.session.commit()
        

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