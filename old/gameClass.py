import json
from openingHelper import findOpening

class Game:
    def __init__(self, pgn, username):
        self.username = username
        self.color, self.opponent = self.determineColor(pgn)
        self.result = self.calculateResult(pgn)
        self.variant = pgn.headers['Variant']
        board = pgn.board()
        self.moves = ''
        for move in pgn.mainline_moves():
            board.push(move)  # make the move on the board
            # Append move in standard algebraic notation to the string
            self.moves += board.san(move) + " "
        self.moves = self.moves.strip()
        self.opening = findOpening(pgn.headers['ECO'], pgn.mainline_moves())

    def determineColor(self, pgn):
        white = pgn.headers['White']
        black = pgn.headers['Black']
        if self.username == white:
            return 'White', black
        elif self.username == black:
            return 'Black', white
        else:
            print('Given user not in game! Defaulting to white player.')
            return 'White', black

    def calculateResult(self, pgn):
        pgnResult = pgn.headers['Result']
        if pgnResult == '1/2-1/2':
            return 'Draw'
        elif pgnResult == '1-0':
            if self.color == 'White':
                return 'Win'
            else: return 'Loss'
        elif pgnResult == '0-1':
            if self.color == 'Black':
                return 'Win'
            else: return 'Loss'
        else:
            print('Unrecognized game result! Defaulting to draw.')
            return 'Draw'