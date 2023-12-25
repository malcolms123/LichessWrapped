import chess.pgn
from gameClass import Game

#username = input('Username?')
username = 'malcolms123'

pgn = open("test.pgn")


games = []
i = 100
moreGames = True
while moreGames:
    nextGame = chess.pgn.read_game(pgn)
    if nextGame is None:
        moreGames = False
    else:
        games.append(Game(nextGame, username))

print(f"{len(games)} games found.")


wins = 0
losses = 0
draws = 0
for game in games:
    if game.result == 'Win':
        wins += 1
    if game.result == 'Loss':
        losses += 1
    if game.result == 'Draw':
        draws += 1

print(wins)
print(losses)
print(draws)

