import json

class PersonalGame:
    def __init__(self, game, username):
        self.username = username.lower()
        self.game = game
        self.color, self.opponent = self.determineColor()
        self.result = self.calculateResult()
        self.openings = self.determineOpenings()

    def determineColor(self):
        white = self.game.white.lower()
        black = self.game.black.lower()
        if self.username == white:
            return 'white', black
        elif self.username == black:
            return 'black', white
        else:
            # maybe this condition should cause the personal game to not exist
            print('Given username not in game! Defaulting to white.')
            return 'white', black

    def calculateResult(self):
        if self.game.result == '1/2-1/2':
            return 'draw'
        elif self.game.result == '1-0':
            if self.color == 'white':
                return 'win'
            else: return 'loss'
        elif self.game.result == '0-1':
            if self.color == 'black':
                return 'win'
            else: return 'loss'
        else:
            print('Unrecognized game result! Defaulting to draw.')
            return 'draw'

    def determineOpenings(self):
        with open('openings.json', 'r', encoding='utf-8') as file:
            openings = json.load(file)
        ecoOpenings = openings.get(self.game.eco)
        gameOpenings = []
        if ecoOpenings is None:
            return gameOpenings
        for opening in ecoOpenings:
            openingMoves = opening.get('moves')
            if self.game.moves[0:len(openingMoves)] == openingMoves:
                gameOpenings.append(opening.get('name'))
        return gameOpenings

        
