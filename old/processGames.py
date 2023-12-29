import chess.pgn
from old.gameClass import Game

# consider finding username from pgn
# should be in every game, should catch error if not in each game

def processGames(pgn, username):
    games = []
    moreGames = True
    while moreGames:
        nextGame = chess.pgn.read_game(pgn)
        if nextGame is None:
            moreGames = False
        else:
            games.append(Game(nextGame, username))
    print(f"{len(games)} games found.")
    return games