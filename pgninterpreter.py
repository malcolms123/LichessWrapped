# This code was written by ChatGPT
# had to do small fixes to correct parsing

import re

class Game:
    def __init__(self, headers, moves):
        # Initialize all possible game attributes
        self.event = headers.get("Event")
        self.site = headers.get("Site")
        self.date = headers.get("Date")
        self.white = headers.get("White")
        self.black = headers.get("Black")
        self.result = headers.get("Result")
        self.utc_date = headers.get("UTCDate")
        self.utc_time = headers.get("UTCTime")
        self.white_elo = headers.get("WhiteElo")
        self.black_elo = headers.get("BlackElo")
        self.white_rating_diff = headers.get("WhiteRatingDiff")
        self.black_rating_diff = headers.get("BlackRatingDiff")
        self.variant = headers.get("Variant")
        self.time_control = headers.get("TimeControl")
        self.eco = headers.get("ECO")
        self.termination = headers.get("Termination")
        # Moves for the game
        self.moves = moves

def clean_moves(moves):
    # Function to clean moves similar to previous examples
    return [move for move in moves if not re.match(r"^\d+\.", move) and move not in ['1-0', '0-1', '1/2-1/2']]

def parse_pgn(pgn_data):
    # Split the PGN data into individual games
    raw_games = pgn_data.strip().split("\n\n\n") # my fix was adding an extra new line character here
    games = []
    for raw_game in raw_games:
        headers = {}
        moves = []
        lines = raw_game.strip().split("\n")
        for line in lines:
            if line.startswith("[") and line.endswith("]"):  # Header line
                key, value = re.findall(r'\[([^ ]+) "(.*?)"\]', line)[0]
                headers[key] = value
            else:
                # Assuming any line not in brackets is a line of moves
                moves.extend(clean_moves(line.split()))
        games.append(Game(headers, moves))
    return games

# Usage example:
# with open("path/to/your/pgn_file.pgn", "r") as file:
#     pgn_data = file.read()
# game_list = parse_pgn(pgn_data)
# for game in game_list:
#     print(vars(game))  # Print game as dictionary for easy viewing
