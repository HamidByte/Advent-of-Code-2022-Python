# read input
input = open('input.txt', 'r')
lines = input.readlines()
opponentTotal = 0
yourTotal = 0

elf = 0
calories = []
for line in lines:
    if (line == '\n'):
        calories.append(elf)
        elf = 0
    else:
        elf = elf + int(line)

if (lines[-1] != '\n'):
    calories.append(elf)

sortedCalories = sorted(calories)
# maxCalories = max(calories)
maxCalories = sortedCalories[-1]

# find the top 3 most calories
threeMostCalories = sortedCalories[-3:]
sumMostCalories = sum(threeMostCalories)

# print(sortedCalories)
# part one
print('Most calories: ', maxCalories)
# part two
print('Sum of three most calories: ', sumMostCalories)