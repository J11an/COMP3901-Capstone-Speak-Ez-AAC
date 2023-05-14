# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired
from flask_wtf.file import FileAllowed,FileRequired

class SavedPhraseForm(FlaskForm):
    saved_phrases = StringField('saved_phrases',validators=[InputRequired()]) 
    category = StringField('category',validators=[InputRequired()])

class WordForm(FlaskForm):
    word = StringField('word',validators=[InputRequired()]) 
    category = StringField('category',validators=[InputRequired()])
    symbol = StringField('symbol',validators=[InputRequired()])
