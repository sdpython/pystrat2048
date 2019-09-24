"""
Implements a random strategy for the game 2048.
"""
import random


def random_strategy(game, moves=None):
    """
    Returns a random direction.

    :param game: matrix usually 4x4 but could anything else
    :param moves: list of previous moves (unused)
    :return: a direction in `{0, 1, 2, 3}`
    """
    return random.randint(0, 3)


def random_strategy_all_but_one(game, moves=None):
    """
    Returns a random direction among three.

    :param game: matrix usually 4x4 but could anything else
    :param moves: list of previous moves (unused)
    :return: a direction in `{0, 1, 2}`
    """
    return random.randint(0, 2)
