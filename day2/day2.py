from types import SimpleNamespace

# access the points with dot notation
points = {
    'ROCK': 1,
    'PAPER': 2,
    'SISSOR': 3,
    'LOST': 0,
    'DRAW': 3,
    'WIN': 6,
}
p = SimpleNamespace(**points)

# access the rules with dot notation
rules = {
    'ROCK': 'ROCK',
    'PAPER': 'PAPER',
    'SISSOR': 'SISSOR',
}
r = SimpleNamespace(**rules)

# replace A,B,C and X,Y,Z with rock, paper, sissor
def getValue(player):
    if (player == 'A' or player == 'X'):
        return r.ROCK
    if (player == 'B' or player == 'Y'):
        return r.PAPER
    if (player == 'C' or player == 'Z'):
        return r.SISSOR

# check win, loss, or draw
def rockPaperSissor(foe, you):
    if (getValue(you) == r.ROCK):
        if (getValue(foe) == r.ROCK):
            return [p.ROCK + p.DRAW, p.ROCK + p.DRAW]
        elif (getValue(foe) == r.PAPER):
            return [p.PAPER + p.WIN, p.ROCK + p.LOST]
        elif (getValue(foe) == r.SISSOR):
            return [p.SISSOR + p.LOST, p.ROCK + p.WIN]
    elif (getValue(you) == r.PAPER):
        if (getValue(foe) == r.ROCK):
            return [p.ROCK + p.LOST, p.PAPER + p.WIN]
        elif (getValue(foe) == r.PAPER):
            return [p.PAPER + p.DRAW, p.PAPER + p.DRAW]
        elif (getValue(foe) == r.SISSOR):
            return [p.SISSOR + p.WIN, p.PAPER + p.LOST]
    elif (getValue(you) == r.SISSOR):
        if (getValue(foe) == r.ROCK):
            return [p.ROCK + p.WIN, p.SISSOR + p.LOST]
        elif (getValue(foe) == r.PAPER):
            return [p.PAPER + p.LOST, p.SISSOR + p.WIN]
        elif (getValue(foe) == r.SISSOR):
            return [p.SISSOR + p.DRAW, p.SISSOR + p.DRAW]

# read input
input = open('input.txt', 'r')
lines = input.readlines()
opponentTotal = 0
yourTotal = 0

for line in lines:
    s = line[:3].split(' ')
    result = rockPaperSissor(s[0], s[1])
    opponentTotal = opponentTotal + result[0]
    yourTotal = yourTotal + result[1]

# part one
print('Opponent\'s total score: ', opponentTotal)
print('Your total score: ', yourTotal)

# part two