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
