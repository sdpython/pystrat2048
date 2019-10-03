"""
Implements the rule the 2048 game.
"""
import random
import numpy


class GameOverException(RuntimeError):
    """
    Raised when the game is over.
    """
    pass


class Game2048State:
    """
    To store additional information while guessing the best
    move.
    """
    def __init__(self, game):
        self.game = game


class Game2048:
    """
    Implements the logic of the game 2048.
    """

    def __init__(self, game=None):
        """
        :param game: None or matrix 4x4
        """
        self.game = (game if game is not None
                     else numpy.zeros((4, 4), dtype=int))
        self.moves = []
        self.state = Game2048State(self)

    def __str__(self):
        "Displays the game as a string."
        if len(self.moves) > 3:
            last_moves = self.moves[-3:]
        else:
            last_moves = self.moves
        return "{}\n{}".format(str(self.game), str(last_moves))

    def gameover(self):
        "Checks the game is over or not. Returns True in that case."
        return numpy.ma.masked_not_equal(self.game, 0).count() == 0

    def copy(self):
        "Makes a copy of the game."
        return Game2048(self.game.copy())

    def next_turn(self):
        "Adds a number in the game."
        if self.gameover():
            raise GameOverException("Game Over\n" + str(self.game))
        else:
            while True:
                i = random.randint(0, self.game.shape[0] - 1)
                j = random.randint(0, self.game.shape[1] - 1)
                if self.game[i, j] == 0:
                    n = random.randint(0, 3)
                    self.game[i, j] = 4 if n == 0 else 2
                    self.moves.append((i, j, self.game[i, j]))
                    break

    @staticmethod
    def process_line(line):
        """
        Moves numbers inside a vector whether this vector represents
        a row or a column.
        """
        res = []
        for n in line:
            if n == 0:
                # Zero: skipped.
                continue
            if len(res) == 0:
                # First number: add.
                res.append(n)
            else:
                prev = res[-1]
                if prev == n:
                    # The number is identical: combine.
                    res[-1] = 2 * n
                else:
                    # Otherwise: add.
                    res.append(n)
        while len(res) < len(line):
            res.append(0)
        return res

    def play(self, direction):
        "Updates the game after a direction was chosen."
        if direction == 0:
            lines = [Game2048.process_line(self.game[i, :])
                     for i in range(self.game.shape[0])]
            self.game = numpy.array(lines)
        elif direction == 1:
            lines = [Game2048.process_line(self.game[:, i])
                     for i in range(self.game.shape[1])]
            self.game = numpy.array(lines).T
        elif direction == 2:
            lines = [list(reversed(Game2048.process_line(self.game[i, ::-1])))
                     for i in range(self.game.shape[0])]
            self.game = numpy.array(lines)
        elif direction == 3:
            lines = [list(reversed(Game2048.process_line(self.game[::-1, i])))
                     for i in range(self.game.shape[1])]
            self.game = numpy.array(lines).T

    def score(self):
        "Returns the maximum values."
        return numpy.max(self.game)

    def best_move(self, game=None, moves=None):
        """
        Selects the best move knowing the current game.
        By default, selects a random direction.
        This function must not modify the game.

        :param game: 4x4 matrix or None for the current matrix
        :param moves: all moves since the begining
        :return: one integer
        """
        if game is None:
            game = self.game
        if moves is None:
            moves = self.moves
        if moves is None:
            raise ValueError("moves cannot be None")
        if not isinstance(game, numpy.ndarray) or game.shape != (4, 4):
            raise ValueError("game must be a matrix (4x4).")
        return random.randint(0, 3)
