# read input
file = 'input.txt'
lines = open(file).read().splitlines()

register = 1
cycles = 1
signalStrength = []

def checkCycle(cycles, register):
    if (cycles % 40 == 20):
        signalStrength.append(cycles * register)

for line in lines:
    if (line == 'noop'):
        cycles += 1
        checkCycle(cycles, register)
    else:
        if (len(line) > 0):
            add = line.split()
        if (add[0] == 'addx'):
            for i in range(2):
                cycles += 1
                if (i == 1):
                    register += int(add[1])
                checkCycle(cycles, register)

# print ('Signal strengths: ', signalStrength)
print ('Sum of signal strengths: ', sum(signalStrength))
