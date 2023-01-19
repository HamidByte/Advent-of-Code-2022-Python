# read input
input = open('input.txt', 'r')
lines = input.readlines()
detected = []

# detect start of packet marker
def startOfPacketMarker(dataStreamBuffer):
    # print(dataStreamBuffer)
    for index in range(len(dataStreamBuffer)):
        marker = dataStreamBuffer[index:index+4]
        if (len(set(marker)) == len(marker)):
            return index + 4

# apply start of packet marker on every line
for line in lines:
    line = line.split()[0]
    detected.append(startOfPacketMarker(line))

# part one
if (len(detected) == 1):
    print('Start of packet marker: ', *detected)
else:
    print('Start of packet marker: ', detected)

# part two