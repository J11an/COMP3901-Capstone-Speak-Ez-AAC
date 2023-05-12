# Add any model classes for Flask-SQLAlchemy here
from . import db
from sqlalchemy import Index

class Words(db.Model):

    word_id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(20), primary_key=True)
    partofspeech = db.Column(db.String(20), primary_key=True)
    category = db.Column(db.String(20))
    grade_level = db.Column(db.String(20))
    time = db.Column(db.String(20))
    place = db.Column(db.String(20))
    symbol= db.Column(db.Text)

    __table_args__ = (
        Index('idx', 'word_id'),
        Index('posidx','partofspeech')
    )

    def __init__(self, word, category, grade_level, partofspeech, time, place,symbol):

        self.word = word
        self.partofspeech = partofspeech
        self.category = category
        self.grade_level = grade_level    
        self.time = time
        self.place = place
        self.symbol = symbol
        

    def __repr__(self):
        return '<Word %r>' % (self.word)

    def get_id(self):
        try:
            return unicode(self.word_id)  # python 2 support
        except NameError:
            return str(self.word_id)  # python 3 support
        
class PartsofSpeech(db.Model):
    pos_id= db.Column(db.String(20),primary_key=True)
    pos=db.Column(db.String(20))

    def __init__(self,pos_id,pos):
        self.pos_id=pos_id
        self.pos=pos

    def __repr__(self):
       return '<PartofSpeech %r>' % (self.pos)

    def get_id(self):
        try:
            return unicode(self.pos_id)  # python 2 support
        except NameError:
            return str(self.pos_id)  # python 3 support
        
class Adjectives(db.Model):
    word_id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(20))
    pos_id= db.Column(db.String(20))
    comparative= db.Column(db.String(20))
    superlative= db.Column(db.String(20))    

    def __init__(self,word_id,word,pos_id,comparative,superlative):
        self.word_id=word_id
        self.word=word
        self.pos_id=pos_id
        self.comparative=comparative
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
    pos_id= db.Column(db.String(20))
    plural=db.Column(db.String(20))
    possessive= db.Column(db.String(20))
    male=db.Column(db.String(20))
    female=db.Column(db.String(20))

    def __init__(self,word_id,word,pos_id,plural,possessive,male,female):
        self.word_id=word_id
        self.word=word
        self.pos_id=pos_id
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
    pos_id= db.Column(db.String(20))
    plural=db.Column(db.String(20))
    past= db.Column(db.String(20))
    present_cont=db.Column(db.String(20))
    future=db.Column(db.String(20))
    perfect=db.Column(db.String(20))

    def __init__(self,word_id,word,pos_id,plural,past,present_cont,future,perfect):
        self.word_id=word_id
        self.word=word
        self.pos_id=pos_id
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

    def __init__(self,symbol_id,symbol):
        self.symbol_id=symbol_id
        self.symbol=symbol

    def __repr__(self):
       return '<Symbols%r>' % (self.symbol)

    def get_id(self):
        try:
            return unicode(self.symbol_id)  # python 2 support
        except NameError:
            return str(self.symbol_id)  # python 3 support

class Pronouns(db.Model):

    word_id= db.Column(db.Integer,primary_key=True)
    word=db.Column(db.String(20))

    def __init__(self,word_id,word):
        self.word_id=word_id
        self.word=word

    def __repr__(self):
       return '<Pronoun%r>' % (self.word)

    def get_id(self):
        try:
            return unicode(self.word_id)  # python 2 support
        except NameError:
            return str(self.word_id)  # python 3 support

class Articles (db.Model):

    word_id= db.Column(db.Integer,primary_key=True)
    word=db.Column(db.String(20))

    def __init__(self,word_id,word):
        self.word_id=word_id
        self.word=word

    def __repr__(self):
       return '<Article%r>' % (self.word)

    def get_id(self):
        try:
            return unicode(self.word_id)  # python 2 support
        except NameError:
            return str(self.word_id)  # python 3 support

class SavedPhrases(db.Model):
    
    saved_phrases_id= db.Column(db.Integer,primary_key=True)
    saved_phrases=db.Column(db.String(80))
    category = db.Column(db.String(20))


    def __init__(self,saved_phrases,category):
            self.saved_phrases=saved_phrases
            self.category=category

    def __repr__(self):
       return '<Saved Phrase%r>' % (self.saved_phrases)

    def get_id(self):
        try:
            return unicode(self.saved_phrases_id)  # python 2 support
        except NameError:
            return str(self.saved_phrases_id)  # python 3 support

class PinnedWords(db.Model):
    
    pinnedwords_id= db.Column(db.Integer,primary_key=True)

    def __init__(self,pinnedwords_id):
            self.pinnedwords_id=pinnedwords_id

    def __repr__(self):
       return '<Pinned Word%r>' % (self.pinnedwords_id)

    def get_id(self):
        try:
            return unicode(self.pinnedwords_id)  # python 2 support
        except NameError:
            return str(self.pinnedwords_id)  # python 3 support
