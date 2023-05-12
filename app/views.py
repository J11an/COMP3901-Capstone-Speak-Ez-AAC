"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, socketio
from flask import abort, render_template, request, jsonify, send_file, send_from_directory
from flask_wtf.csrf import generate_csrf
import os
from app.models import *
from .forms import *
from werkzeug.utils import secure_filename
from app.Scripts.tts import *
from app.Scripts.vosk_speech_rec import *
from vosk import Model, KaldiRecognizer
import pandas as pd
import numpy as np
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

# Speaking Screen
@app.route('/api/speak', methods=['POST'])
def speak():
    if request.method == 'POST':
        text = request.form['speech']
        gender = request.form['voices']
        # rate = request.form['speed']
        text_to_speech(text, gender)
        mp3 = os.path.join(rootdir, r"message.mp3")
        return send_file(mp3, mimetype='audio/mp3', as_attachment=True)


@app.route('/api/word_associated/', methods=['POST', 'GET'])
def word_associated():
    next_partsofspeech = {}

    query = request.args.get('word')
    
    # query = "red"

    tiles = Words.query.filter_by(word=query).all()
    for tile in tiles:

        if tile.partofspeech == 'Noun':
            next_partsofspeech["adjectives"] = [{"id": adjectives.word_id, "word": adjectives.word, "symbol": adjectives.symbol,} for adjectives in
                                                Words.query.filter_by(partofspeech='Adjectives').order_by(
                                                    func.random()).group_by(Words.word_id).limit(4).all()]
            next_partsofspeech["preposition"] = [{"id": preposition.word_id, "word": preposition.word, "symbol": preposition.symbol,} for preposition in
                                                Words.query.filter_by(partofspeech='Preposition').order_by(
                                                    func.random()).group_by(Words.word_id).limit(4).all()]
            next_partsofspeech["conjunction"] = [{"id": conjunction.word_id, "word": conjunction.word, "symbol": conjunction.symbol,} for conjunction in
                                                Words.query.filter_by(partofspeech='Conjunction').order_by(
                                                    func.random()).group_by(Words.word_id).limit(4).all()]
            next_partsofspeech["verb"] = [{"id": verb.word_id, "word": verb.word, "symbol": verb.symbol,} for verb in
                                            Words.query.filter_by(partofspeech='Verb').order_by(func.random()).group_by(Words.word_id).limit(4).all()]
            next_partsofspeech["noun"] = [{"id": noun.word_id, "word": noun.word, "symbol": noun.symbol,} for noun in
                                            Words.query.filter_by(partofspeech='Noun').order_by(func.random()).group_by(Words.word_id).limit(4).all()]

        if tile.partofspeech == 'Articles':
            next_partsofspeech["adjectives"] = [{"id": adjectives.word_id, "word": adjectives.word, "symbol": adjectives.symbol,} for adjectives in
                                                Words.query.filter_by(partofspeech='Adjectives').order_by(
                                                    func.random()).group_by(Words.word_id).limit(4).all()]
            next_partsofspeech["noun"] = [{"id": noun.word_id, "word": noun.word, "symbol": noun.symbol,} for noun in
                                            Words.query.filter_by(partofspeech='Noun').order_by(func.random()).group_by(Words.word_id).limit(4).all()]

        if tile.partofspeech == 'Pronoun':
            next_partsofspeech["preposition"] = [{"id": preposition.word_id, "word": preposition.word, "symbol": preposition.symbol,} for preposition in
                                                Words.query.filter_by(partofspeech='Preposition').order_by(
                                                    func.random()).group_by(Words.word_id).limit(4).all()]
            next_partsofspeech["verb"] = [{"id": verb.word_id, "word": verb.word, "symbol": verb.symbol,} for verb in
                                            Words.query.filter_by(partofspeech='Verb').order_by(func.random()).group_by(Words.word_id).limit(4).all()]
            next_partsofspeech["noun"] = [{"id": noun.word_id, "word": noun.word, "symbol": noun.symbol,} for noun in
                                            Words.query.filter_by(partofspeech='Noun').order_by(func.random()).group_by(Words.word_id).limit(4).all()]
        if tile.partofspeech == 'Preposition':
            next_partsofspeech["articles"] = [{"id": articles.word_id, "word": articles.word, "symbol": articles.symbol,} for articles in
                                                Words.query.filter_by(partofspeech='Articles').order_by(func.random()).group_by(Words.word_id).limit(
                                                    4).all()]
            next_partsofspeech["noun"] = [{"id": noun.word_id, "word": noun.word, "symbol": noun.symbol,} for noun in
                                            Words.query.filter_by(partofspeech='Noun').order_by(func.random()).group_by(Words.word_id).limit(4).all()]
            next_partsofspeech["pronoun"] = [{"id": pronoun.word_id, "word": pronoun.word, "symbol": pronoun.symbol,} for pronoun in
                                                Words.query.filter_by(partofspeech='Pronoun').order_by(func.random()).group_by(Words.word_id).limit(
                                                    4).all()]

        if tile.partofspeech == 'Conjunction':
            next_partsofspeech["verb"] = [{"id": verb.word_id, "word": verb.word, "symbol": verb.symbol,} for verb in
                                            Words.query.filter_by(partofspeech='Verb').order_by(func.random()).group_by(Words.word_id).limit(4).all()]
            next_partsofspeech["articles"] = [{"id": articles.word_id, "word": articles.word, "symbol": articles.symbol,} for articles in
                                                Words.query.filter_by(partofspeech='Articles').order_by(func.random()).group_by(Words.word_id).limit(
                                                    4).all()]
            next_partsofspeech["pronoun"] = [{"id": pronoun.word_id, "word": pronoun.word, "symbol": pronoun.symbol,} for pronoun in
                                                Words.query.filter_by(partofspeech='Pronoun').order_by(func.random()).group_by(Words.word_id).limit(
                                                    4).all()]

        if tile.partofspeech == 'Adjectives':
            next_partsofspeech["adjectives"] = [{"id": adjectives.word_id, "word": adjectives.word, "symbol": adjectives.symbol,} for adjectives in
                                                Words.query.filter_by(partofspeech='Adjectives').order_by(
                                                    func.random()).group_by(Words.word_id).limit(4).all()]
            next_partsofspeech["conjunction"] = [{"id": conjunction.word_id, "word": conjunction.word, "symbol": conjunction.symbol,} for conjunction in
                                                Words.query.filter_by(partofspeech='Conjunction').order_by(
                                                    func.random()).limit(4).all()]
            next_partsofspeech["noun"] = [{"id": noun.word_id, "word": noun.word, "symbol": noun.symbol,} for noun in
                                            Words.query.filter_by(partofspeech='Noun').order_by(func.random()).group_by(Words.word_id).limit(4).all()]

        if tile.partofspeech == 'Verb':
            next_partsofspeech["adjectives"] = [{"id": adjectives.word_id, "word": adjectives.word, "symbol": adjectives.symbol,} for adjectives in
                                                Words.query.filter_by(partofspeech='Adjectives').order_by(
                                                    func.random()).group_by(Words.word_id).limit(4).all()]
            next_partsofspeech["preposition"] = [{"id": preposition.word_id, "word": preposition.word, "symbol": preposition.symbol,} for preposition in
                                                    Words.query.filter_by(partofspeech='Preposition').order_by(
                                                        func.random()).group_by(Words.word_id).limit(4).all()]
            next_partsofspeech["articles"] = [{"id": articles.word_id, "word": articles.word, "symbol": articles.symbol,} for articles in
                                                Words.query.filter_by(partofspeech='Articles').order_by(func.random()).group_by(Words.word_id).limit(
                                                    4).all()]
            next_partsofspeech["verb"] = [{"id": verb.word_id, "word": verb.word, "symbol": verb.symbol,} for verb in
                                            Words.query.filter_by(partofspeech='Verb').order_by(func.random()).group_by(Words.word_id).limit(4).all()]
            next_partsofspeech["noun"] = [{"id": noun.word_id, "word": noun.word, "symbol": noun.symbol,} for noun in
                                            Words.query.filter_by(partofspeech='Noun').order_by(func.random()).group_by(Words.word_id).limit(4).all()]
            next_partsofspeech["pronoun"] = [{"id": pronoun.word_id, "word": pronoun.word, "symbol": pronoun.symbol,} for pronoun in
                                                Words.query.filter_by(partofspeech='Pronoun').order_by(func.random()).group_by(Words.word_id).limit(
                                                    4).all()]


    return jsonify(next_partsofspeech), 200
    

@app.route('/api/search/<word>', methods=['GET'])
def search_word(word):
    if request.method == 'GET':
        matched = []
        search_result = Words.query.filter(Words.word.ilike(f'%{word}%')).all()
        # n specifies the maximum number of closest matches to return and
        # cutoff is specifies a threshold for how closely a word needs to match the input word to be considered a match between 0 and 1
        matches = [(w.word_id, w.symbol, w.word) for w in search_result]
        matches = list(set(get_close_matches(word, [match[2] for match in matches], n=30, cutoff=0.1)))

        for match in matches:
            for word in search_result:
                if word.word == match and word.word_id not in [mword['id'] for mword in matched]:
                    matched.append({"id": word.word_id,"word": word.word,"symbol": word.symbol})
        return jsonify(matched)
    
@app.route('/api/inital_tree_setting', methods=['GET'])
def inital_tree_setting():
    columns = {
    }
    columns["noun"] = [{"id": noun.word_id, "word": noun.word, "symbol": noun.symbol,} for noun in
                                Words.query.filter_by(partofspeech='Noun').order_by(func.random()).group_by(Words.word_id).limit(4).all()]
    columns["verb"] = [{"id": verb.word_id, "word": verb.word, "symbol": verb.symbol,} for verb in
                                    Words.query.filter_by(partofspeech='Verb').order_by(func.random()).group_by(Words.word_id).limit(4).all()]
    columns["adjectives"] = [{"id": adjectives.word_id, "word": adjectives.word, "symbol": adjectives.symbol,} for adjectives in
                                        Words.query.filter_by(partofspeech='Adjectives').order_by(
                                            func.random()).group_by(Words.word_id).limit(4).all()]
    columns["articles"] = [{"id": articles.word_id, "word": articles.word, "symbol": articles.symbol,} for articles in
                                        Words.query.filter_by(partofspeech='Articles').order_by(func.random()).group_by(Words.word_id).limit(
                                            4).all()]
    columns["pronoun"] = [{"id": pronoun.word_id, "word": pronoun.word, "symbol": pronoun.symbol,} for pronoun in
                                        Words.query.filter_by(partofspeech='Pronoun').order_by(func.random()).group_by(Words.word_id).limit(
                                            4).all()]

    return jsonify(columns), 201


@app.route('/api/get_categories', methods=['GET'])
def get_catergories():
    categories = db.session.query(Words.category).distinct().all()
    categories = [c[0] for c in categories]
    return jsonify(categories)


@app.route('/api/get_word_symbol', methods=['GET'])
def get_word_symbol():
    
    reqword = request.args.get('word')
    word = Words.query.filter_by(word=reqword).first()
    if word == None:
        return jsonify({'error':"Word is not in database"})
    else:
        result = {
                'word': word.word,
                'id': word.word_id,
                'symbol': word.symbol
            }
    return jsonify(result)

@app.route('/api/get_categories_group/<string:word>')
def get_categories_group(word):
    word=Words.query.filter_by(word=word).all()
    categories=set([w.category for w in word])
    result=[]
    for category in categories:
        categories_words=word[w for w in words if w.category==category]
        category_info=[{
            'id':w.word_id,
            'symbol':w.symbol,
            'words':w.word
        }for w in categories_words]

        result[category]=category_info
    return jsonify({word:result})
    
        
    



# Listening Screen
@app.route('/api/listen', methods=['POST'])
def listen():
    if request.method == 'POST':
        data = request.data
        rec.AcceptWaveform(data)
        result = rec.Result()
        result_json = jsonify({"text": result})
        return result_json


# Saved Phrases
@app.route('/api/saved_phrases',methods=['POST','GET','PUT','DELETE'])
def phrases():
        id = request.args.get('id')
        form = SavedPhraseForm()    
        if request.method == 'POST':
            if form.validate_on_submit():
                saved_phrases = request.form['saved_phrases']
                category = request.form['category']
                exists = db.session.query(SavedPhrases.saved_phrases_id ).filter_by(saved_phrases=saved_phrases).first() is not None
                if exists == False:
                    savedphrase = SavedPhrases(saved_phrases,category)
                    db.session.add(savedphrase)
                    db.session.commit()     
                    return jsonify({"message": 'Saved Phrase Added'}), 201  
                else:
                    return jsonify({"error": 'Phrase already exists'})
            return jsonify(errors=form_errors(form))
        if request.method == 'GET': 
            categories = [category[0] for category in db.session.query(SavedPhrases.category).distinct()]
            phrases_by_category = {category: [{"id" : phrase.saved_phrases_id ,"word" : phrase.saved_phrases,} for phrase in SavedPhrases.query.filter_by(category=category).all()] for category in categories}        
            return jsonify(phrases_by_category),201
        if request.method == 'PUT':
            if form.validate_on_submit():
                phrase = SavedPhrases.query.filter_by(saved_phrases_id=id).first()
                if not phrase:
                    return jsonify({'message': 'Phrase not found'}), 404
                saved_phrases = request.form['saved_phrases']
                category = request.form['category']
                phrase.saved_phrases = saved_phrases
                phrase.category = category
                db.session.commit()
                return jsonify({'message': 'Saved Phrase Updated'}), 200
            return jsonify(errors=form_errors(form))
        if request.method == 'DELETE':
            phrase = SavedPhrases.query.filter_by(saved_phrases_id=id).first()
            if not phrase:
                return jsonify({'message': 'Phrase not found'}), 404
            db.session.delete(phrase)
            db.session.commit()
            return jsonify({'message': 'Saved Phrase Deleted'}), 200
        

# @app.route('/api/word',methods=['POST','GET','PUT','DELETE'])
# def words():
#         id = request.args.get('id')
#         form = WordForm()    
#         if request.method == 'POST':
#             if form.validate_on_submit():
#                 word = request.form['word']
#                 category = request.form['category']
#                 symbol = request.form['word']
#                 exists = db.session.query(Words.word_id ).filter_by(word=word).first() is not None
#                 if exists == False:
#                     savedphrase = Words(saved_phrases,category)
#                     db.session.add(savedphrase)
#                     db.session.commit()     
#                     return jsonify({"message": 'Saved Phrase Added'}), 201  
#                 else:
#                     return jsonify({"error": 'Phrase already exists'})
#             return jsonify(errors=form_errors(form))
#         if request.method == 'GET': 
#             categories = [category[0] for category in db.session.query(SavedPhrases.category).distinct()]
#             phrases_by_category = {category: [{"id" : phrase.saved_phrases_id ,"word" : phrase.saved_phrases,} for phrase in SavedPhrases.query.filter_by(category=category).all()] for category in categories}        
#             return jsonify(phrases_by_category),201
#         if request.method == 'PUT':
#             if form.validate_on_submit():
#                 phrase = SavedPhrases.query.filter_by(saved_phrases_id=id).first()
#                 if not phrase:
#                     return jsonify({'message': 'Phrase not found'}), 404
#                 saved_phrases = request.form['saved_phrases']
#                 category = request.form['category']
#                 phrase.saved_phrases = saved_phrases
#                 phrase.category = category
#                 db.session.commit()
#                 return jsonify({'message': 'Saved Phrase Updated'}), 200
#             return jsonify(errors=form_errors(form))
#         if request.method == 'DELETE':
#             phrase = SavedPhrases.query.filter_by(saved_phrases_id=id).first()
#             if not phrase:
#                 return jsonify({'message': 'Phrase not found'}), 404
#             db.session.delete(phrase)
#             db.session.commit()
#             return jsonify({'message': 'Saved Phrase Deleted'}), 200

        
# Seed Vocab List
@app.route('/api/seed_database')
def seed_database():
    # Change file path to the one on your computer (Temp Maybe). Lol use os.path
    df = pd.read_excel(f"{os.path.abspath(os.getcwd())}\\app\\Vocab list.xlsx", sheet_name=None)

    if db.session.query(Words).count():
        return {"message" : "database already exists"}, 202
    else:
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
                        symbol=(row['symbol']),

                    )
                    db.session.add(cword)
                    db.session.commit()

            try:
                if sheet_name == "Parts_of_speech":
                    for index, row in sheet_data.iterrows():
                        cpartofspeech = PartsofSpeech(
                            pos_id=(row['pos_id']),
                            pos=(row['pos'])
                        )
                        db.session.add(cpartofspeech)
                        db.session.commit()
                if sheet_name == "Adjectives":
                    for index, row in sheet_data.iterrows():
                        cAdjectives = Adjectives(
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
                        cNoun = Nouns(
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
                        cVerb = Verbs(
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
                        cSymbol = Symbols(
                            symbol_id=(row['symbol_id']),
                            symbol=(row['symbol'])
                        )
                        db.session.add(cSymbol)
                        db.session.commit()
                if sheet_name == "Pronouns":
                    for index, row in sheet_data.iterrows():
                        cPronoun = Pronouns(
                            word_id=(row['word_id']),
                            word=(row['word'])
                        )
                        db.session.add(cPronoun)
                        db.session.commit()
                if sheet_name == "Articles":
                    for index, row in sheet_data.iterrows():
                        cArticle = Articles(
                            word_id=(row['word_id']),
                            word=(row['word'])
                        )
                        db.session.add(cArticle)
                        db.session.commit()
            except Exception as e:
                print(f"DB Exception {e}")
        return {"success" : "database seeded"}, 202

@app.route('/api/csrf-token',methods=["GET"])
def get_csrf():
    return jsonify({'csrf_token' : generate_csrf()})

@app.route('/api/pinned_words',methods=["GET","POST"])
def pinned_words():
    if request.method == "GET":
        pwords = db.session.execute(db.select(PinnedWords)).scalars()
        pwords_list = [{"id": pword.pinnedwords_id} for pword in pwords]
        return jsonify(pwords_list), 200
    
    if request.method == "POST":
        pinnedword_id = request.args.get('word_id')
        cPinnedWords = PinnedWords(pinnedword_id)
        db.session.add(cPinnedWords)
        db.session.commit()

        return {"success" : "pinned word added"},201
    
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
