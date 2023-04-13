# Add any model classes for Flask-SQLAlchemy here
from . import db


class Tile(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(20))
    partofspeech = db.Column(db.String(20))
    category = db.Column(db.String(20))
    time = db.Column(db.String(20))
    place = db.Column(db.String(20))
    plural = db.Column(db.String(20))
    photo = db.Column(db.String(100))

    def __init__(self, word, category, partofspeech, time, place, plural, photo):

        self.word = word
        self.partofspeech = partofspeech
        self.category = category
        self.time = time
        self.place = place
        self.plural = plural
        self.photo = photo

    def __repr__(self):
        return '<Tile %r>' % (self.word)

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support


class Words(db.Model):

    word_id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(20))
    partofspeech = db.Column(db.String(20))
    category = db.Column(db.String(20))
    time = db.Column(db.String(20))
    place = db.Column(db.String(20))
    symbol_id= db.Column(db.String(20))

    def __init__(self, word, category, partofspeech, time, place, symbol_id):

        self.word = word
        self.partofspeech = partofspeech
        self.category = category
        self.time = time
        self.place = place
        self.symbol_id = symbol_id
        

    def __repr__(self):
        return '<Tile %r>' % (self.word)

    def get_id(self):
        try:
            return unicode(self.word_id)  # python 2 support
        except NameError:
            return str(self.word_id)  # python 3 support
    



class Tense (db.Model):
    tense_id=db.Column(db.Integer,primary_key=True)
    word_id=db.Column(db.Integer)
    past_tense=db.Column(db.String(20))
    present_tense=db.Column(db.String(20))
    pretense_continuous=db.Column(db.String(20))
    future_tense=db.Column(db.String(20))

    def __init__(self,word_id,past_tense,present_tense,pretense_continuous,future_tense):
        
        self.word_id=word_id
        self.past_tense=past_tense
        self.present_tense=present_tense
        self.pretense_continuous=pretense_continuous
        self.future_tense=future_tense

    def __repr__(self):
       return '<Tense %r>' % (self.tense_id)

    def get_id(self):
        try:
            return unicode(self.tense_id)  # python 2 support
        except NameError:
            return str(self.tense_id)  # python 3 support
        
class Plurals(db.Model):
    plural_id=db.Column(db.Integer,primary_key=True)
    word_id=db.Column(db.Integer)
    plural=db.Column(db.String(20))

    def __init__(self,plural,word_id):
        self.plural=plural
        self.word_id=word_id

    def __repr__(self):
       return '<Plurals%r>' % (self.plural)

    def get_id(self):
        try:
            return unicode(self.plural_id)  # python 2 support
        except NameError:
            return str(self.plural_id)  # python 3 support

class Symbols(db.Model):
    word_id=db.Column(db.Integer)
    symbol_id= db.Column(db.Integer,primary_key=True)
    symbol=db.Column(db.String(20))

    def __init__(self,word_id,symbol):
        self.word_id=word_id
        self.symbol=symbol

    def __repr__(self):
       return '<Symbols%r>' % (self.symbol)

    def get_id(self):
        try:
            return unicode(self.symbol_id)  # python 2 support
        except NameError:
            return str(self.symbol_id)  # python 3 support

class PartofSpeech(db.Model):
    partofspeech_id= db.Column(db.Integer,primary_key=True)
    partofspeech=db.Column(db.String(20))

    def __init__(self,partofspeech):
        self.partofspeech=partofspeech

    def __repr__(self):
       return '<PartofSpeech %r>' % (self.partofspeech)

    def get_id(self):
        try:
            return unicode(self.partofspeech_id)  # python 2 support
        except NameError:
            return str(self.partofspeech_id)  # python 3 support


