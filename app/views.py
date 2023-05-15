"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, socketio
from flask import (
    abort,
    render_template,
    request,
    jsonify,
    send_file,
    send_from_directory,
)
from flask_wtf.csrf import generate_csrf
import os
from app.models import *
from werkzeug.utils import secure_filename
from app.Scripts.tts import *
from app.Scripts.vosk_speech_rec import *
from vosk import Model, KaldiRecognizer
import pandas as pd
from sqlalchemy import func
from difflib import get_close_matches

phrases = []
rootdir = os.getcwd()
model_dir = os.path.join(rootdir + r"\model\vosk-model-small-en-us-0.15")
model = Model(model_dir)
rec = KaldiRecognizer(model, 16000)


###
# Routing for your application.
###g


@app.route("/")
def index():
    return jsonify(message="This is the beginning of our API")


###
# The functions below should be applicable to all Flask apps.
###


# Speaking Screen
@app.route("/api/speak", methods=["POST"])
def speak():
    if request.method == "POST":
        text = request.form["speech"]
        gender = request.form["voices"]
        # rate = request.form['speed']
        text_to_speech(text, gender)
        mp3 = os.path.join(rootdir, r"message.mp3")
        return send_file(mp3, mimetype="audio/mp3", as_attachment=True)


@app.route("/api/word_associated/", methods=["POST", "GET"])
def word_associated():
    next_partsofspeech = {}

    query = request.args.get("word")
    query = query.replace("%20", " ")

    tiles = Words.query.filter_by(word=query).all()
    for tile in tiles:
        if tile.partofspeech == "Noun":
            next_partsofspeech["adjectives"] = [
                {
                    "id": adjectives.word_id,
                    "word": adjectives.word,
                    "symbol": adjectives.symbol,
                }
                for adjectives in Words.query.filter_by(partofspeech="Adjectives")
                .order_by(func.random())
                .group_by(Words.word_id)
                .limit(4)
                .all()
            ]
            next_partsofspeech["preposition"] = [
                {
                    "id": preposition.word_id,
                    "word": preposition.word,
                    "symbol": preposition.symbol,
                }
                for preposition in Words.query.filter_by(partofspeech="Preposition")
                .order_by(func.random())
                .group_by(Words.word_id)
                .limit(4)
                .all()
            ]
            next_partsofspeech["conjunction"] = [
                {
                    "id": conjunction.word_id,
                    "word": conjunction.word,
                    "symbol": conjunction.symbol,
                }
                for conjunction in Words.query.filter_by(partofspeech="Conjunction")
                .order_by(func.random())
                .group_by(Words.word_id)
                .limit(4)
                .all()
            ]
            next_partsofspeech["verb"] = [
                {
                    "id": verb.word_id,
                    "word": verb.word,
                    "symbol": verb.symbol,
                }
                for verb in Words.query.filter_by(partofspeech="Verb")
                .order_by(func.random())
                .group_by(Words.word_id)
                .limit(4)
                .all()
            ]
            next_partsofspeech["noun"] = [
                {
                    "id": noun.word_id,
                    "word": noun.word,
                    "symbol": noun.symbol,
                }
                for noun in Words.query.filter_by(partofspeech="Noun")
                .order_by(func.random())
                .group_by(Words.word_id)
                .limit(4)
                .all()
            ]

        if tile.partofspeech == "Articles":
            adjectives = [
                {
                    "id": adjectives.word_id,
                    "word": adjectives.word,
                    "symbol": adjectives.symbol,
                }
                for adjectives in Words.query.filter_by(partofspeech="Adjectives")
                .order_by(func.random())
                .group_by(Words.word_id)
                .limit(8)
                .all()
            ]
            noun = [
                {
                    "id": noun.word_id,
                    "word": noun.word,
                    "symbol": noun.symbol,
                }
                for noun in Words.query.filter_by(partofspeech="Noun")
                .order_by(func.random())
                .group_by(Words.word_id)
                .limit(8)
                .all()
            ]
            next_partsofspeech["noun"], next_partsofspeech["noun2"] = noun[:4], noun[4:]
            next_partsofspeech["adjectives"], next_partsofspeech["adjectives2"] = (
                adjectives[:4],
                adjectives[4:],
            )

        if tile.partofspeech == "Pronoun":
            next_partsofspeech["preposition"] = [
                {
                    "id": preposition.word_id,
                    "word": preposition.word,
                    "symbol": preposition.symbol,
                }
                for preposition in Words.query.filter_by(partofspeech="Preposition")
                .order_by(func.random())
                .group_by(Words.word_id)
                .limit(4)
                .all()
            ]
            verb = [
                {
                    "id": verb.word_id,
                    "word": verb.word,
                    "symbol": verb.symbol,
                }
                for verb in Words.query.filter_by(partofspeech="Verb")
                .order_by(func.random())
                .group_by(Words.word_id)
                .limit(8)
                .all()
            ]
            noun = [
                {
                    "id": noun.word_id,
                    "word": noun.word,
                    "symbol": noun.symbol,
                }
                for noun in Words.query.filter_by(partofspeech="Noun")
                .order_by(func.random())
                .group_by(Words.word_id)
                .limit(8)
                .all()
            ]
            next_partsofspeech["verb"], next_partsofspeech["verb2"] = verb[:4], verb[4:]
            next_partsofspeech["noun"], next_partsofspeech["noun2"] = noun[:4], noun[4:]

        if tile.partofspeech == "Preposition":
            next_partsofspeech["articles"] = [
                {
                    "id": articles.word_id,
                    "word": articles.word,
                    "symbol": articles.symbol,
                }
                for articles in Words.query.filter_by(partofspeech="Articles")
                .order_by(func.random())
                .group_by(Words.word_id)
                .limit(4)
                .all()
            ]
            noun = [
                {
                    "id": noun.word_id,
                    "word": noun.word,
                    "symbol": noun.symbol,
                }
                for noun in Words.query.filter_by(partofspeech="Noun")
                .order_by(func.random())
                .group_by(Words.word_id)
                .limit(8)
                .all()
            ]
            next_partsofspeech["pronoun"] = [
                {
                    "id": pronoun.word_id,
                    "word": pronoun.word,
                    "symbol": pronoun.symbol,
                }
                for pronoun in Words.query.filter_by(partofspeech="Pronoun")
                .order_by(func.random())
                .group_by(Words.word_id)
                .limit(4)
                .all()
            ]
            next_partsofspeech["noun"], next_partsofspeech["noun2"] = noun[:4], noun[4:]

        if tile.partofspeech == "Conjunction":
            verb = [
                {
                    "id": verb.word_id,
                    "word": verb.word,
                    "symbol": verb.symbol,
                }
                for verb in Words.query.filter_by(partofspeech="Verb")
                .order_by(func.random())
                .group_by(Words.word_id)
                .limit(8)
                .all()
            ]
            next_partsofspeech["articles"] = [
                {
                    "id": articles.word_id,
                    "word": articles.word,
                    "symbol": articles.symbol,
                }
                for articles in Words.query.filter_by(partofspeech="Articles")
                .order_by(func.random())
                .group_by(Words.word_id)
                .limit(4)
                .all()
            ]
            next_partsofspeech["pronoun"] = [
                {
                    "id": pronoun.word_id,
                    "word": pronoun.word,
                    "symbol": pronoun.symbol,
                }
                for pronoun in Words.query.filter_by(partofspeech="Pronoun")
                .order_by(func.random())
                .group_by(Words.word_id)
                .limit(4)
                .all()
            ]
            next_partsofspeech["verb"], next_partsofspeech["verb2"] = verb[:4], verb[4:]

        if tile.partofspeech == "Adjectives":
            next_partsofspeech["adjectives"] = [
                {
                    "id": adjectives.word_id,
                    "word": adjectives.word,
                    "symbol": adjectives.symbol,
                }
                for adjectives in Words.query.filter_by(partofspeech="Adjectives")
                .order_by(func.random())
                .group_by(Words.word_id)
                .limit(4)
                .all()
            ]
            next_partsofspeech["conjunction"] = [
                {
                    "id": conjunction.word_id,
                    "word": conjunction.word,
                    "symbol": conjunction.symbol,
                }
                for conjunction in Words.query.filter_by(partofspeech="Conjunction")
                .order_by(func.random())
                .limit(4)
                .all()
            ]
            noun = [
                {
                    "id": noun.word_id,
                    "word": noun.word,
                    "symbol": noun.symbol,
                }
                for noun in Words.query.filter_by(partofspeech="Noun")
                .order_by(func.random())
                .group_by(Words.word_id)
                .limit(8)
                .all()
            ]
            next_partsofspeech["noun"], next_partsofspeech["noun2"] = noun[:4], noun[4:]

        if tile.partofspeech == "Verb":
            next_partsofspeech["adjectives"] = [
                {
                    "id": adjectives.word_id,
                    "word": adjectives.word,
                    "symbol": adjectives.symbol,
                }
                for adjectives in Words.query.filter_by(partofspeech="Adjectives")
                .order_by(func.random())
                .group_by(Words.word_id)
                .limit(4)
                .all()
            ]
            next_partsofspeech["preposition"] = [
                {
                    "id": preposition.word_id,
                    "word": preposition.word,
                    "symbol": preposition.symbol,
                }
                for preposition in Words.query.filter_by(partofspeech="Preposition")
                .order_by(func.random())
                .group_by(Words.word_id)
                .limit(4)
                .all()
            ]
            next_partsofspeech["articles"] = [
                {
                    "id": articles.word_id,
                    "word": articles.word,
                    "symbol": articles.symbol,
                }
                for articles in Words.query.filter_by(partofspeech="Articles")
                .order_by(func.random())
                .group_by(Words.word_id)
                .limit(4)
                .all()
            ]
            next_partsofspeech["verb"] = [
                {
                    "id": verb.word_id,
                    "word": verb.word,
                    "symbol": verb.symbol,
                }
                for verb in Words.query.filter_by(partofspeech="Verb")
                .order_by(func.random())
                .group_by(Words.word_id)
                .limit(4)
                .all()
            ]
            next_partsofspeech["noun"] = [
                {
                    "id": noun.word_id,
                    "word": noun.word,
                    "symbol": noun.symbol,
                }
                for noun in Words.query.filter_by(partofspeech="Noun")
                .order_by(func.random())
                .group_by(Words.word_id)
                .limit(4)
                .all()
            ]
            next_partsofspeech["pronoun"] = [
                {
                    "id": pronoun.word_id,
                    "word": pronoun.word,
                    "symbol": pronoun.symbol,
                }
                for pronoun in Words.query.filter_by(partofspeech="Pronoun")
                .order_by(func.random())
                .group_by(Words.word_id)
                .limit(4)
                .all()
            ]

    return jsonify(next_partsofspeech), 200


@app.route("/api/search/<word>", methods=["GET"])
def search_word(word):
    if request.method == "GET":
        matched = []
        search_result = Words.query.filter(Words.word.ilike(f"%{word}%")).all()
        # n specifies the maximum number of closest matches to return and
        # cutoff is specifies a threshold for how closely a word needs to match the input word to be considered a match between 0 and 1
        matches = [(w.word_id, w.symbol, w.word) for w in search_result]
        matches = list(
            set(
                get_close_matches(
                    word, [match[2] for match in matches], n=30, cutoff=0.1
                )
            )
        )

        for match in matches:
            for word in search_result:
                if word.word == match and word.word_id not in [
                    mword["id"] for mword in matched
                ]:
                    matched.append(
                        {"id": word.word_id, "word": word.word, "symbol": word.symbol}
                    )
        return jsonify(matched)


@app.route("/api/inital_tree_setting", methods=["GET"])
def inital_tree_setting():
    columns = {}
    columns["noun"] = [
        {
            "id": noun.word_id,
            "word": noun.word,
            "symbol": noun.symbol,
            "category": noun.category,
        }
        for noun in Words.query.filter_by(partofspeech="Noun")
        .order_by(func.random())
        .group_by(Words.word_id)
        .limit(4)
        .all()
    ]
    columns["verb"] = [
        {
            "id": verb.word_id,
            "word": verb.word,
            "symbol": verb.symbol,
            "category": verb.category,
        }
        for verb in Words.query.filter_by(partofspeech="Verb")
        .order_by(func.random())
        .group_by(Words.word_id)
        .limit(4)
        .all()
    ]
    columns["adjectives"] = [
        {
            "id": adjectives.word_id,
            "word": adjectives.word,
            "symbol": adjectives.symbol,
            "category": adjectives.category,
        }
        for adjectives in Words.query.filter_by(partofspeech="Adjectives")
        .order_by(func.random())
        .group_by(Words.word_id)
        .limit(4)
        .all()
    ]
    columns["articles"] = [
        {
            "id": articles.word_id,
            "word": articles.word,
            "symbol": articles.symbol,
            "category": articles.category,
        }
        for articles in Words.query.filter_by(partofspeech="Articles")
        .order_by(func.random())
        .group_by(Words.word_id)
        .limit(4)
        .all()
    ]
    columns["pronoun"] = [
        {
            "id": pronoun.word_id,
            "word": pronoun.word,
            "symbol": pronoun.symbol,
            "category": pronoun.category,
        }
        for pronoun in Words.query.filter_by(partofspeech="Pronoun")
        .order_by(func.random())
        .group_by(Words.word_id)
        .limit(4)
        .all()
    ]

    return jsonify(columns), 201


@app.route("/api/get_categories", methods=["GET"])
def get_catergories():
    categories = db.session.query(Words.category).distinct().all()
    categories = [c[0] for c in categories]
    return jsonify(categories)


@app.route("/api/get_phrase_categories", methods=["GET"])
def get_phrase_categories():
    categories = db.session.query(SavedPhrases.category).distinct().all()
    categories = [c[0] for c in categories]
    return jsonify(categories)


@app.route("/api/get_word_symbol", methods=["GET"])
def get_word_symbol():
    reqword = request.args.get("word")
    word = Words.query.filter_by(word=reqword).first()
    if word == None:
        return jsonify({"error": "Word is not in database"})
    else:
        result = {
            "word": word.word,
            "id": word.word_id,
            "symbol": word.symbol,
            "category": word.category,
        }
    return jsonify(result)


@app.route("/api/get_categories_group/<string:word>", methods=["GET"])
def get_categories_group(word):
    word = Words.query.filter_by(word=word).all()
    result = {}
    for w in word:
        category = w.category
        if category not in result:
            result[category] = []
        result[category].append({"word": w.word, "id": w.word_id, "symbol": w.symbol})

    return jsonify({word: result})


@app.route("/api/get_grade_level", methods=["GET"])
def get_grade_level():
    grade_level = request.args.get("grade_level")

    if grade_level == "upper":
        words = Words.query.filter(Words.grade_level.in_(["upper", "lower"])).all()
    else:
        words = Words.query.filter_by(grade_level="lower").all()

    results = [{"word": g.word, "id": g.word_id, "symbol": g.symbol} for g in words]

    return jsonify(results)


# Listening Screen
@app.route("/api/listen", methods=["POST"])
def listen():
    if request.method == "POST":
        data = request.data
        rec.AcceptWaveform(data)
        result = rec.Result()
        result_json = jsonify({"text": result})
        return result_json


# Saved Phrases
@app.route("/api/saved_phrases", methods=["POST", "GET", "PUT", "DELETE"])
def phrases():
    id = request.args.get("id")

    if request.method == "POST":
        saved_phrases = request.args.get("saved_phrases").lower()
        category = request.args.get("category").lower()
        exists = (
            db.session.query(SavedPhrases.saved_phrases_id)
            .filter_by(saved_phrases=saved_phrases)
            .first()
            is not None
        )
        num_categories = db.session.query(
            db.func.count(db.distinct(SavedPhrases.category))
        ).scalar()
        if exists == False and num_categories < 10 and category != "":
            savedphrase = SavedPhrases(saved_phrases, category)
            db.session.add(savedphrase)
            db.session.commit()
            return jsonify({"message": "Saved Phrase Added"}), 201
        else:
            return jsonify(
                {"error": "Phrase already exists or there are 10 categories"}
            )

    if request.method == "GET":
        category = request.args.get("category")

        phrases = [
            {"id": phrase.saved_phrases_id, "word": phrase.saved_phrases}
            for phrase in SavedPhrases.query.filter_by(category=category).all()
        ]

        return jsonify(phrases), 201

    if request.method == "PUT":
        phrase = SavedPhrases.query.filter_by(saved_phrases_id=id).first()
        if not phrase:
            return jsonify({"message": "Phrase not found"}), 404
        saved_phrases = request.args.get("saved_phrases")
        category = request.args.get("category")
        if (
            saved_phrases != ""
            and category != ""
            and saved_phrases != None
            and category != None
        ):
            phrase.saved_phrases = saved_phrases
            phrase.category = category
            db.session.commit()
            return jsonify({"message": "Saved Phrase Updated"}), 201
        return jsonify({"message": "Phrase or Category field is blank"})

    if request.method == "DELETE":
        phrase = SavedPhrases.query.filter_by(saved_phrases_id=id).first()
        if not phrase:
            return jsonify({"message": "Phrase not found"}), 404
        db.session.delete(phrase)
        db.session.commit()
        return jsonify({"message": "Saved Phrase Deleted"}), 201


@app.route("/api/fetch_category_symbols")
def fetch_category_symbols():
    categories = [
        category[0].lower()
        for category in db.session.query(SavedPhrases.category).distinct()
    ]
    phrases_by_category = {}
    for category in categories:
        query = (
            db.session.query(Words.symbol)
            .outerjoin(SavedPhrases, Words.word == SavedPhrases.saved_phrases)
            .filter(Words.word == category)
            .all()
        )
        print(query)
        if query != []:
            phrases_by_category[category] = [
                {"symbol": phrase.symbol} for phrase in query
            ]
        elif query == []:
            phrases_by_category[category] = [{"symbol": "public\HelpIcon.png"}]

    return jsonify(phrases_by_category)


@app.route("/api/word", methods=["POST", "GET", "PUT", "DELETE"])
def words():
    id = request.args.get("id")

    if request.method == "POST":
        word = request.args.get("word")
        symbol = request.args.get("symbol")
        category = request.args.get("category")
        exists = (
            db.session.query(Words.word_id).filter_by(word=word).first() is not None
        )
        if exists == False and word != "" and word != None:
            word = Words(word, category, "", "", "", "", symbol)
            db.session.add(word)
            db.session.commit()
            return jsonify({"message": "Word Added"}), 201
        else:
            if word == "" or word == None:
                return jsonify({"error": "Word field is empty"})
            return jsonify({"error": "Word already exists"})

    if request.method == "GET":
        words = Words.query.all()
        words = [
            {
                "id": word.word_id,
                "word": word.word,
                "partofspeech": word.partofspeech,
                "category": word.category,
                "symbols": word.symbol,
            }
            for word in words
        ]
        return jsonify(words), 201

    if request.method == "PUT":
        word = Words.query.filter_by(word_id=id).first()
        if not word:
            return jsonify({"message": "Word not found"}), 404
        cword = request.args.get("word")
        symbol = request.args.get("symbol")
        category = request.args.get("category")
        if cword != "" and cword != None:
            word.word = cword
            word.category = category
            word.symbol = symbol
            db.session.commit()
            return jsonify({"message": "Word Updated"}), 201
        else:
            return jsonify({"error": "Word field is blank"}), 201

    if request.method == "DELETE":
        word = Words.query.filter_by(word_id=id).first()
        if not word:
            return jsonify({"message": "Word not found"}), 404
        db.session.delete(word)
        db.session.commit()
        return jsonify({"message": "Word Deleted"}), 201


@app.route("/api/check_message")
def check_message():
    saved_phrases = request.args.get("saved_phrases").lower()
    exists = (
        db.session.query(SavedPhrases.saved_phrases_id)
        .filter_by(saved_phrases=saved_phrases)
        .first()
        is not None
    )
    if exists == True and saved_phrases != "":
        return jsonify({"message": "Phrase exists"}), 201
    return jsonify({"message": "Phrase does not exist"})


# Seed Vocab List
@app.route("/api/seed_database")
def seed_database():
    # Change file path to the one on your computer (Temp Maybe). Lol use os.path
    df = pd.read_excel(
        f"{os.path.abspath(os.getcwd())}\\app\\Vocab list.xlsx", sheet_name=None
    )

    if db.session.query(Words).count():
        return {"message": "database already exists"}, 202
    else:
        for sheet_name, sheet_data in df.items():
            if sheet_name == "Words":
                for index, row in sheet_data.iterrows():
                    cword = Words(
                        word=str(row["word"]).lower()
                        if isinstance(row["word"], str)
                        else row["word"],
                        partofspeech=(row["part_of_speech"]),
                        category=(row["category"]),
                        grade_level=(row["grade_level"]),
                        time=(row["time"]),
                        place=(row["place"]),
                        symbol=(row["symbol"]),
                    )
                    db.session.add(cword)
                    db.session.commit()
            if sheet_name == "CensoredTerms":
                for index, row in sheet_data.iterrows():
                    cterm = CensoredTerms(
                        term=str(row["term"]).lower()
                        if isinstance(row["term"], str)
                        else row["term"],
                    )
                    db.session.add(cterm)
                    db.session.commit()
            if sheet_name == "SavedPhrases":
                for index, row in sheet_data.iterrows():
                    cPhrase = SavedPhrases(
                        saved_phrases=str(row["saved_phrases"]).lower()
                        if isinstance(row["saved_phrases"], str)
                        else row["saved_phrases"],
                        category=str(row["category"]).lower()
                        if isinstance(row["category"], str)
                        else row["category"],
                    )
                    db.session.add(cPhrase)
                    db.session.commit()

            try:
                if sheet_name == "Parts_of_speech":
                    for index, row in sheet_data.iterrows():
                        cpartofspeech = PartsofSpeech(
                            pos_id=(row["pos_id"]), pos=(row["pos"])
                        )
                        db.session.add(cpartofspeech)
                        db.session.commit()
                if sheet_name == "Adjectives":
                    for index, row in sheet_data.iterrows():
                        cAdjectives = Adjectives(
                            word_id=(row["word_id"]),
                            word=(row["word"]),
                            pos_id=(row["pos_id"]),
                            comparative=(row["comparative"]),
                            superlative=(row["superlative"]),
                        )
                        db.session.add(cAdjectives)
                        db.session.commit()
                if sheet_name == "Nouns":
                    for index, row in sheet_data.iterrows():
                        cNoun = Nouns(
                            word_id=(row["word_id"]),
                            word=(row["word"]),
                            pos_id=(row["pos_id"]),
                            plural=(row["plural"]),
                            possessive=(row["possessive"]),
                            male=(row["male"]),
                            female=(row["Female"]),
                        )
                        db.session.add(cNoun)
                        db.session.commit()
                if sheet_name == "Verbs":
                    for index, row in sheet_data.iterrows():
                        cVerb = Verbs(
                            word_id=(row["word_id"]),
                            word=(row["word"]),
                            pos_id=(row["pos_id"]),
                            plural=(row["plural"]),
                            past=(row["past"]),
                            present_cont=(row["present_cont"]),
                            future=(row["future"]),
                            perfect=(row["perfect"]),
                        )
                        db.session.add(cVerb)
                        db.session.commit()
                if sheet_name == "Symbols":
                    for index, row in sheet_data.iterrows():
                        cSymbol = Symbols(
                            symbol_id=(row["symbol_id"]), symbol=(row["symbol"])
                        )
                        db.session.add(cSymbol)
                        db.session.commit()
                if sheet_name == "Pronouns":
                    for index, row in sheet_data.iterrows():
                        cPronoun = Pronouns(
                            word_id=(row["word_id"]), word=(row["word"])
                        )
                        db.session.add(cPronoun)
                        db.session.commit()
                if sheet_name == "Articles":
                    for index, row in sheet_data.iterrows():
                        cArticle = Articles(
                            word_id=(row["word_id"]), word=(row["word"])
                        )
                        db.session.add(cArticle)
                        db.session.commit()
            except Exception as e:
                print(f"DB Exception {e}")
        return {"success": "database seeded"}, 202


@app.route("/api/csrf-token", methods=["GET"])
def get_csrf():
    return jsonify({"csrf_token": generate_csrf()})


@app.route("/api/pinned_words", methods=["GET", "POST", "DELETE"])
def pinned_words():
    if request.method == "GET":
        pwords = PinnedWords.query.all()
        pinned_word_list = []
        for pword in pwords:
            word = Words.query.filter_by(word_id=pword.pinnedwords_id).first()
            if word:
                pinned_word_list.append(
                    {
                        "id": pword.pinnedwords_id,
                        "word": word.word,
                        "symbol": word.symbol,
                    }
                )
        return jsonify(pinned_word_list), 201

    if request.method == "POST":
        pinnedwords_id = request.args.get("word_id")
        cPinnedWords = PinnedWords(pinnedwords_id)
        db.session.add(cPinnedWords)
        db.session.commit()

        return {"success": "Pinned word added"}, 201

    if request.method == "DELETE":
        id = request.args.get("id")
        pword = PinnedWords.query.filter_by(pinnedwords_id=id).first()
        if not pword:
            return jsonify({"message": "Pinned Word not found"}), 404
        db.session.delete(pword)
        db.session.commit()
        return jsonify({"message": "Pinned Word Deleted"}), 200


@app.route("/api/filter_words", methods=["GET", "POST"])
def filter():
    cterms = set([row.term for row in CensoredTerms.query.all()])
    message = request.args.get("message")
    message = message.lower()
    words = message.split()
    filtered_words = [word for word in words if word not in cterms]
    return jsonify(filtered_words), 201


# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = "Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error,
            )
            error_messages.append(message)

    return error_messages


@app.route("/<file_name>.txt")
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + ".txt"
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers["X-UA-Compatible"] = "IE=Edge,chrome=1"
    response.headers["Cache-Control"] = "public, max-age=0"
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return jsonify(error="Page Not Found"), 404
