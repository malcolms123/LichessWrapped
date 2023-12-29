import json, re

openingsPath = 'openings.json'

def queryECO(eco):
    with open(openingsPath, 'r', encoding='utf-8') as file:
        openings = json.load(file)
    
    # Retrieve the opening(s) for the given ECO code
    ecoOpenings = openings.get(eco)
    return ecoOpenings

def find_longest_match(game_moves, opening_list):
    longest_match = None
    max_length = 0

    for opening in opening_list:
        # Splitting both the game moves and opening moves into arrays
        opening_moves = opening['moves'].split()
        game_move_sequence = game_moves.split()

        # Find how many moves match at the start of the sequence
        match_length = sum(1 for i, move in enumerate(opening_moves) if i < len(game_move_sequence) and move == game_move_sequence[i])

        # Update the longest match if this one is longer
        if match_length > max_length:
            max_length = match_length
            longest_match = opening['name']

    return longest_match



def findOpening(eco, moves):
    moves = re.sub(r'\d+\. ', '', moves).strip()
    openings = queryECO(eco)
    return find_longest_match(moves, openings)