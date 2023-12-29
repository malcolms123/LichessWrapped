import pgninterpreter

# with open("path/to/your/pgn_file.pgn", "r") as file:
#     pgn_data = file.read()
# game_list = parse_pgn(pgn_data)
# for game in game_list:
#     print(vars(game))  # Print game as dictionary for easy viewing

with open('test.pgn', 'r') as file:
    pgn_data = file.read()
games = pgninterpreter.parse_pgn(pgn_data)

print(games[-1].moves)