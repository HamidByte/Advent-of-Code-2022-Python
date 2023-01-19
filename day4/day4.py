# read input
input = open('input.txt', 'r')
lines = input.readlines()
sectionOverlapIds = 0
someOverlapIds = 0

def firstToLast(str):
    list = str.split('-')
    return [x for x in range(int(list[0]), int(list[1]) + 1)]

for line in lines:
    line = line.split('\n')[0]
    line = line.split(',')
    firstStr = line[0]
    secondStr = line[1]
    firstList = firstToLast(firstStr)
    secondList = firstToLast(secondStr)
    if (all(item in firstList for item in secondList) or all(item in secondList for item in firstList)):
        sectionOverlapIds = sectionOverlapIds + 1
    if (any(item in firstList for item in secondList) or any(item in secondList for item in firstList)):
        someOverlapIds = someOverlapIds + 1

# part one
print('Total overlapping section IDs: ', sectionOverlapIds)
# part two
print('Some overlapping section IDs: ', someOverlapIds)