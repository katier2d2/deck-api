import random
import json
import string
from flask import jsonify
from flask_restplus import abort

import models


suits = ['SPADES', 'DIAMONDS', 'CLUBS', 'HEARTS']
values = ['2', '3', '4', '5', '6', '7', '8', '9', 'JACK', 'QUEEN', 'KING', 'ACE']
NEW_DECK = {}
i = 1

for suit in suits:
    for value in values:
        NEW_DECK[i] = {
            "suit": suit,
            "value": value,
            "code": value[0]+suit[0]
        }
        i += 1


def get(id):
    deck_data = models.Decks.query.filter(models.Decks.deck_id == id).one_or_none()
    if deck_data is None:
        abort(404, 'Deck not found for id: {id}'.format(id=id))
    return deck_data


def get_deck(id):
    if id == 'new':
        abort(405, 'Method not allowed, use POST to create new deck')

    deck_data = get(id)

    resp = deck_data.serialize
    resp["success"] = True

    return jsonify(resp)


def create(id, shuffle=False):
    if not id == 'new':
        abort(405, 'Method not allowed, only allow deck creation on "new" requests')

    deck_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
    cards = list(NEW_DECK.keys())
    if shuffle:
        random.shuffle(cards)

    deck_data = models.Decks(
        deck_id=deck_id,
        shuffled=shuffle,
        remaining=len(cards),
        cards=json.dumps(cards),
    )
    models.db.session.add(deck_data)
    models.db.session.commit()

    resp = deck_data.serialize
    resp["success"] = True

    return jsonify(resp)


def shuffle(id):
    if id == 'new':
        abort(405, 'Method not allowed, use POST to create new shuffled deck')

    deck_data = get(id)
    cards = json.loads(deck_data.cards)
    random.shuffle(cards)

    deck_data.deck_id = id
    deck_data.shuffled = True
    deck_data.remaining = len(cards)
    deck_data.cards = json.dumps(cards)

    models.db.session.commit()

    resp = deck_data.serialize
    resp["success"] = True

    return jsonify(resp)


def draw(id, count):
    deck_data = get(id)
    cards = json.loads(deck_data.cards)
    cards_drawn = []

    for i in range(0, count):
        drawn_card = cards.pop(i)
        drawn_card_data = NEW_DECK.get(drawn_card, None)
        cards_drawn.append(drawn_card_data)

    deck_data.deck_id = id
    deck_data.shuffled = True
    deck_data.remaining = len(cards)
    deck_data.cards = json.dumps(cards)

    models.db.session.commit()

    resp = deck_data.serialize
    resp["success"] = True
    resp["cards"] = cards_drawn

    return jsonify(resp)
