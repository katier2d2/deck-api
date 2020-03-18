from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.hybrid import hybrid_property


db = SQLAlchemy()

# TODO: UUID for id
class Decks(db.Model):
    __tablename__ = 'decks'
    id = db.Column(db.Integer, primary_key=True)
    deck_id = db.Column(db.String, nullable=False)
    shuffled = db.Column(db.Boolean, nullable=False)
    remaining = db.Column(db.Integer, nullable=False)
    cards = db.Column(db.String, nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'deck_id': self.deck_id,
            'shuffled': self.shuffled,
            'remaining': self.remaining,
            'cards': self.cards
        }
