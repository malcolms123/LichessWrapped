import pgninterpreter, personalgame

pgn_path = 'test.pgn'
username = 'malcolms123'

with open(pgn_path) as file:
    pgn_data = file.read()
pgnGames = pgninterpreter.parse_pgn(pgn_data)

personalGames = []
for game in pgnGames:
    personalGames.append(personalgame.PersonalGame(game, username))

for game in personalGames:
    print(game.openings)