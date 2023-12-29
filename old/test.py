from old.processGames import processGames

# maybe should determine username from file?
username = 'malcolms123'
file = open('test.pgn')

games = processGames(file, username)


def countOccurrences(games, property):
    countDict = {}
    for game in games:
        value = getattr(game, property)
        if value in countDict:
            countDict[value] += 1
        else: 
            countDict[value] = 1
    return countDict


openings = countOccurrences(games, 'opening')
variants = countOccurrences(games, 'variant')
print(openings)