# read input

with open('input.txt', 'r') as file:
    data = file.read().strip().split('\n')

# 
for line in data:
    print(line)
