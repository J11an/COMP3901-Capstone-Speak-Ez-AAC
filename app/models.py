# Add any model classes for Flask-SQLAlchemy here
from . import db

class Words(db.Model):

    word_id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(20))
    partofspeech = db.Column(db.String(20),db.ForeignKey('partsof_speech.partofspeech_id'))
    category = db.Column(db.String(20))
    sub_category = db.Column(db.String(20))
    time = db.Column(db.String(20))
    place = db.Column(db.String(20))
    symbol_id= db.Column(db.Integer,db.ForeignKey('symbols.symbol_id'))

    def __init__(self, word, category, sub_category, partofspeech, time, place, symbol_id):

        self.word = word
        self.partofspeech = partofspeech
        self.category = category
        self.sub_category = sub_category    
        self.time = time
        self.place = place
        self.symbol_id = symbol_id
        

    def __repr__(self):
        return '<Word %r>' % (self.word)

    def get_id(self):
        try:
            return unicode(self.word_id)  # python 2 support
        except NameError:
            return str(self.word_id)  # python 3 support
        
class PartsofSpeech(db.Model):
    partofspeech_id= db.Column(db.String(20),primary_key=True)
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
        
class Adjectives(db.Model):
    word_id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(20))
    pos_id= db.Column(db.String(20),db.ForeignKey('partsof_speech.partofspeech_id'))
    comparitive= db.Column(db.String(20))
    superlative= db.Column(db.String(20))    

    def __init__(self,word_id,word,pos_id,comparitive,superlative):
        self.word_id=word_id
        self.word_id=word
        self.pos_id=pos_id
        self.comparitive=comparitive
        self.superlative=superlative

    def __repr__(self):
       return '<Adjectives %r>' % (self.word)

    def get_id(self):
        try:
            return unicode(self.word_id)  # python 2 support
        except NameError:
            return str(self.word_id)  # python 3 support

class Nouns(db.Model):
        
    word_id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(20))
    pos_id= db.Column(db.String(20),db.ForeignKey('partsof_speech.partofspeech_id'))
    plural=db.Column(db.String(20))
    possessive= db.Column(db.String(20))
    male=db.Column(db.String(20))
    female=db.Column(db.String(20))

    def __init__(self,word,pos_id,plural,possessive,male,female):
        self.plural=word
        self.word_id=pos_id
        self.plural=plural
        self.possessive=possessive
        self.male=male
        self.female=female

    def __repr__(self): 
       return '<Plurals%r>' % (self.word)

    def get_id(self):
        try:
            return unicode(self.word_id)  # python 2 support
        except NameError:
            return str(self.word_id)  # python 3 support
        
class Verbs(db.Model):
        
    word_id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(20))
    pos_id= db.Column(db.String(20),db.ForeignKey('partsof_speech.partofspeech_id'))
    plural=db.Column(db.String(20))
    past= db.Column(db.String(20))
    present_cont=db.Column(db.String(20))
    future=db.Column(db.String(20))
    perfect=db.Column(db.String(20))

    def __init__(self,word,pos_id,plural,past,present_cont,future,perfect):
        self.plural=word
        self.word_id=pos_id
        self.plural=plural
        self.past=past
        self.present_cont=present_cont
        self.future=future
        self.perfect=perfect

    def __repr__(self): 
       return '<Plurals%r>' % (self.word)

    def get_id(self):
        try:
            return unicode(self.word_id)  # python 2 support
        except NameError:
            return str(self.word_id)  # python 3 support

class Symbols(db.Model):

    symbol_id= db.Column(db.Integer,primary_key=True)
    symbol=db.Column(db.String(20))

    def __init__(self,symbol):
        self.symbol=symbol

    def __repr__(self):
       return '<Symbols%r>' % (self.symbol)

    def get_id(self):
        try:
            return unicode(self.symbol_id)  # python 2 support
        except NameError:
            return str(self.symbol_id)  # python 3 support
