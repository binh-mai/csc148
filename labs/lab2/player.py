class Player:
    """ Create a player in a game.

    === Attributes ===
    name: Name of player
    scores: History of their most recent 100 scores

    === Sample Usage ===

    create a Player:
    >>> player_1 = Player('Binh')
    >>> player_1.name
    'Binh'

    add scores to Player's history of scores:
    >>> player_1.add_score([200, 300, 400, 300, 250])
    >>> player_1.scores
    [423, 321, 532, 274, 593]

    get Player's average scores:
    >>> player_1.avg_score(3)  # take in number of most recent game
    300

    get Player's top score"
    >>> player_1.top_score() # no input
    400
    """

    # Attribute types
    name: str
    scores: list[int] # scores = [] initially
