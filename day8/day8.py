# read input
with open('input.txt', 'r') as file:
    data = file.read().strip().split('\n')

totalVisibleTrees = 0
rows = len(data)
columns = len(data[0])
edges = rows * 2 + columns * 2 - 4
totalVisibleTrees = edges
totalScenicScore = []

for row in range(1, rows - 1):
  for col in range(1, columns - 1):
    tree = data[row][col]
    up = [data[row - i][col] for i in range(1, row + 1)]
    down = [data[row + i][col] for i in range(1, rows - row)]
    left = [data[row][col - i] for i in range(1, col + 1)]
    right = [data[row][col + i] for i in range(1, columns - col)]

    # part 1
    if (max(left) < tree or max(right) < tree or max(up) < tree or max(down) < tree):
      totalVisibleTrees += 1

    # part 2
    scenicScore = 1
    for list in (up, down, left, right):
      count = 0
      for i in range(len(list)):
        if (list[i] < tree):
          count = count + 1
        else:
          count = count + 1
          break
      scenicScore = scenicScore * count
    totalScenicScore.append(scenicScore)

# part 1
print('Total number of visible trees: ', totalVisibleTrees)

# part 2
highestScenicScore = max(totalScenicScore)
print('Highest scenic score: ', highestScenicScore)