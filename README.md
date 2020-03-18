# deck-api
An API that creates, deals, shuffles a deck of cards


## Usage


### Create new deck, optional shuffle

**Definition**

`POST /api/deck/new/`
`POST /api/deck/new/shuffle/`

**Response**

- `200 OK` on success

```json
{
  "cards": "[1, 2, 3, 4, ...]",
  "deck_id": "X2WUZC4CJ3QK",
  "id": 1,
  "remaining": 48,
  "shuffled": false,
  "success": true
}
```

### Get existing deck

**Definition**

`GET /api/deck/<string:deck_id>/`

**Response**

- `200 OK` on success
- `404 Not Found` if the deck id does not exist

```json
{
  "cards": "[1, 2, 3, 4, ...]",
  "deck_id": "X2WUZC4CJ3QK",
  "id": 1,
  "remaining": 48,
  "shuffled": false,
  "success": true
}
```


### Shuffle existing deck

**Definition**

`PUT /api/deck/<string:deck_id>/shuffle/`

**Response**

- `204 OK` on success
- `404 Not Found` if the deck id does not exist

```json
{
  "cards": "[15, 39, 20, 47, ...]",
  "deck_id": "X2WUZC4CJ3QK",
  "id": 1,
  "remaining": 48,
  "shuffled": true,
  "success": true
}
```


### Draw cards from existing deck

**Definition**

`PUT /api/deck/<string:deck_id>/draw/`

**Arguments**

- `"count":integer` number of cards to draw

**Response**

- `204 OK` on success
- `404 Not Found` if the deck id does not exist

```json
{
  "cards": [
    {
      "code": "2S",
      "suit": "SPADES",
      "value": "2"
    },
    {
      "code": "4S",
      "suit": "SPADES",
      "value": "4"
    }
  ],
  "deck_id": "X2WUZC4CJ3QK",
  "id": 1,
  "remaining": 46,
  "shuffled": true,
  "success": true
}
```

