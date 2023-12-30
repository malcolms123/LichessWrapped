import pgninterpreter, personalgame

pgn_path = 'test.pgn'
username = 'malcolms123'

with open(pgn_path) as file:
    pgn_data = file.read()
pgnGames = pgninterpreter.parse_pgn(pgn_data)

personalGames = []
for game in pgnGames:
    personalGames.append(personalgame.PersonalGame(game, username))

total_games = len(personalGames)
total_wins = 0
total_draws = 0
total_losses = 0
total_white = 0
total_black = 0
white_wins = 0
white_draws = 0
white_losses = 0
black_wins = 0
black_draws = 0
black_losses = 0
variants = {}

for game in personalGames:
    if game.game.variant in variants:
        variants[game.game.variant] += 1
    else:
        variants[game.game.variant] = 1
    if game.color == 'white':
        total_white += 1
    else:
        total_black += 1
    if game.result == 'win':
        total_wins += 1
        if game.color == 'white':
            white_wins += 1
        else:
            black_wins += 1
    elif game.result == 'loss':
        total_losses += 1
        if game.color == 'white':
            white_losses += 1
        else:
            black_losses += 1
    else:
        total_draws += 1
        if game.color == 'white':
            white_draws += 1
        else:
            black_draws += 1

print('-----PAGE ONE-----')
print(f'{total_games} games played.')
print(f'{total_wins}|{total_draws}|{total_losses}')
print('-----PAGE TWO-----')
print('need to build time control logic')
print('-----PAGE THREE-----')
print(f'White {white_wins}|{white_draws}|{white_losses} ({round(100*white_wins/total_white,1)}% wins)')
print(f'Black {black_wins}|{black_draws}|{black_losses} ({round(100*black_wins/total_black,1)}% wins)')
print('-----PAGE FOUR-----')
print('need to fix openings issues')

print(variants)