# read input
input = open('input.txt', 'r')
lines = input.readlines()
priority = []

def strToNumber(char):
    if (char.islower()):
        return ord(char) - 96
    if (char.isupper()):
        return ord(char) - 38

for line in lines:
    line = line.split('\n')[0]
    half = int(len(line) / 2)
    first = line[0:half]
    second = line[half:]
    for f in first:
        if (second.find(f) != -1):
            priority.append(strToNumber(f))
            break

# part one
allPriorities = sum(priority)
print('Sum of all priorities: ', allPriorities)

# part two
group = []
common = []
groupPriorities = []

for i in range(int(len(lines) / 3)):
    group.append(lines[i*3:(i+1)*3])
    contained = set.intersection(*map(set, group[i]))
    common.append(''.join(list(contained)))

for c in common:
    groupPriorities.append(strToNumber(*c.split()))

print('Sum of priorities in group of three: ', sum(groupPriorities))
