import os

from models import db


def create(app):
    if os.path.exists('decks.db'):
        os.remove('decks.db')

    db.init_app(app)
    app.app_context().push()
    db.create_all()
