import os

from flask import Flask, request
from flask_restplus import Api, Resource, fields

from deck import deck, create


app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ['SQLALCHEMY_TRACK_MODIFICATIONS']
app.config['ERROR_404_HELP'] = False

create(app)

deck_model = api.model("deck_model", {
    "deck_id": fields.String(required=False),
    "shuffled": fields.String(required=False),
    "remaining": fields.Integer(required=False),
    "cards": fields.List(fields.String, required=False)
})


@api.route('/api/deck/<string:deck_id>/')
class GetDeck(Resource):
    @api.response(200, 'deck retrieved')
    @api.response(404, 'deck not found')
    @api.doc('Get deck')
    def get(self, deck_id):
        return deck.get_deck(deck_id)

    @api.response(200, 'new deck created')
    @api.doc('Brand new deck')
    def post(self, deck_id):
        return deck.create(deck_id)


@api.route('/api/deck/<string:deck_id>/shuffle/')
class ReShuffleDeck(Resource):
    @api.response(200, 'deck updated')
    @api.response(404, 'deck not found')
    @api.doc('Re-shuffle the deck')
    def put(self, deck_id):
        return deck.shuffle(deck_id)

    @api.response(200, 'new deck created and shuffled')
    @api.doc('New shuffled deck')
    def post(self, deck_id):
        return deck.create(deck_id, shuffle=True)


@api.route('/api/deck/<string:deck_id>/draw/')
@api.doc('Draw a card/s')
class Draw(Resource):
    @api.response(200, 'deck updated')
    @api.response(404, 'deck not found')
    def put(self, deck_id):
        return deck.draw(deck_id, request.json['count'])


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
