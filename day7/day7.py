import os

# read input
input = open('dummy.txt', 'r')
lines = input.readlines()
directories = {}
directorySize = {}
fileSystem = {}
totalSize = 0

# apply
for line in lines:
    line = line.split('\n')[0]
    if (line[0] == '$'):
        ds, command, *directory = line.split()
        if (command == 'cd'):
            path = directory[0]
            if (path == '/'):
                currentDirectory = path
            else:
                currentDirectory = os.path.normpath(os.path.join(currentDirectory, path))
            if (currentDirectory not in directories):
                directories[currentDirectory] = []
                fileSystem[currentDirectory] = {
                    "path": [],
                    "size": 0,
                    "files": {
                        "name": [],
                        "size": []
                    }
                }
                directorySize[currentDirectory] = 0
    else:
        fileSize, fileName = line.split()
        if (fileSize != 'dir'):
            directorySize[currentDirectory] += int(fileSize)
            fileSystem[currentDirectory]['size'] += int(fileSize)
            fileSystem[currentDirectory]['files']['name'].append(fileName)
            fileSystem[currentDirectory]['files']['size'].append(int(fileSize))
        else:
            directories[currentDirectory].append(os.path.normpath(os.path.join(currentDirectory, fileName)))
            fileSystem[currentDirectory]['path'].append(os.path.normpath(os.path.join(currentDirectory, fileName)))

# compute directory sizes
def computeDirectorySize(dirName: str):
    dirSize = directorySize[dirName]
    for item in directories[dirName]:
        if item in directories:
            dirSize += computeDirectorySize(item)
    return dirSize

for item in directories:
    dirSize = computeDirectorySize(item)
    if dirSize <= 100000:
        totalSize += dirSize

# second way
total = 0
def compute(name):
    size = fileSystem[name]['size']
    for i in fileSystem[name]['path']:
        if i in fileSystem:
            size += compute(i)
    return size

for key in fileSystem:
    size = compute(key)
    if size <= 100000:
        total += size

# print(fileSystem)
# print(directories)
# print(directorySize)
print(totalSize)
print(total)