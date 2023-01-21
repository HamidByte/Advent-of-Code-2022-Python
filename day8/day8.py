# read input

with open('input.txt', 'r') as file:
    data = file.read().strip().split('\n')

# part 1
totalVisibleTrees = 0
rows = len(data)
columns = len(data[0])
edges = rows * 2 + columns * 2 - 4
totalVisibleTrees = edges

for row in range(1, rows - 1):
  for col in range(1, columns - 1):
    tree = data[row][col]
    left = [data[row][col - i] for i in range(1, col + 1)]
    right = [data[row][col + i] for i in range(1, columns - col)]
    up = [data[row - i][col] for i in range(1, row + 1)]
    down = [data[row + i][col] for i in range(1, rows - row)]

    if (max(left) < tree or max(right) < tree or max(up) < tree or max(down) < tree):
      totalVisibleTrees += 1

print('Total number of visible trees: ', totalVisibleTrees)
