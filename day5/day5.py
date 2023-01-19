from collections import defaultdict

# read input
input = open('input.txt', 'r')
lines = input.readlines()

# variables
stacksOfCrates = []
procedures = False
stackColumns = defaultdict(list)
topCrates = ''

# get indices of crates
def getCrateIndex(columnIndex):
    return columnIndex * 4 - 3

# construct list of stacks of marked crates
for index, line in enumerate(lines):
    line = line.split('\n')[0]
    if (line == ''):
        break
    else:
        stacksOfCrates.append(line)

totalColumns = int(stacksOfCrates[-1].split()[-1])
stacksOfCrates = stacksOfCrates[:-1]

# construct dictionary of stacks of marked crates
for stackRow in stacksOfCrates:
    for columnIndex in range(1, totalColumns + 1):
        crateIndex = getCrateIndex(columnIndex)
        if (stackRow[crateIndex] != ' '):
            stackColumns[columnIndex].append(stackRow[crateIndex])

# print(stackColumns)

# rearrange crates in stacks of marked crates
def rearrangeCrates(cratesQuantity, fromStack, toStack):
    cratesMoved = stackColumns[fromStack][0:cratesQuantity]
    del stackColumns[fromStack][0:cratesQuantity]
    for crates in cratesMoved:
        stackColumns[toStack].insert(0, crates)

# apply set of procedures
for line in lines:
    line = line.split('\n')[0]
    if (procedures):
        procedureList = line.split()
        cratesQuantity = int(procedureList[1])
        fromStack = int(procedureList[3])
        toStack = int(procedureList[5])
        rearrangeCrates(cratesQuantity, fromStack, toStack)
    if (line == ''):
        procedures = True

# print(stackColumns)

for key in range(1, len(stackColumns) + 1):
    topCrates += stackColumns[key][0]

# part one
print('Top crates: ', topCrates)

# part two