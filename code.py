import copy
file1 = open('input.txt', 'r')

lines = file1.readlines()
stoneFormation = []
lineOfRocks = []
for line in lines:
    lineOfRocks = line.strip().split(" -> ")
    for i in range(len(lineOfRocks) - 1):
        # get coordinates
        startX = int(lineOfRocks[i].split(",")[0])
        startY = int(lineOfRocks[i].split(",")[1])
        endX = int(lineOfRocks[i+1].split(",")[0])
        endY = int(lineOfRocks[i+1].split(",")[1])        
        if startX == endX:
            if startY < endY:
                for y in range(startY, endY + 1):
                    stoneFormation.append([startX, y])
            if startY > endY:
                for y in range(endY, startY + 1):
                    stoneFormation.append([startX, y])
        if startY == endY:
            if startX < endX:
                for x in range(startX, endX + 1):
                    stoneFormation.append([x, startY])
            if startX > endX:
                for x in range(endX, startX + 1):
                    stoneFormation.append([x, startY])
backupStoneFormation = copy.deepcopy(stoneFormation)
#Part 1
# Find abyss
maxY = 0
for y in range(len(stoneFormation)):
    if maxY < stoneFormation[y][1]:
        maxY = stoneFormation[y][1]
# Simulation for sand falling
sandCoordinates = []
count = 0
while(True):
    sandCoordinates.insert(0, [500,0])
    while(sandCoordinates[0][1] < maxY):
        if [sandCoordinates[0][0], sandCoordinates[0][1] + 1] in stoneFormation:
            if [sandCoordinates[0][0] - 1, sandCoordinates[0][1] + 1 ] in stoneFormation:
                if [sandCoordinates[0][0] + 1, sandCoordinates[0][1] + 1] in stoneFormation:
                    stoneFormation.append([sandCoordinates[0][0], sandCoordinates[0][1]])
                    break
                else:
                    sandCoordinates[0][0] = sandCoordinates[0][0] + 1
                    sandCoordinates[0][1] = sandCoordinates[0][1] + 1                        
            else:
                sandCoordinates[0][0] = sandCoordinates[0][0] - 1
                sandCoordinates[0][1] = sandCoordinates[0][1] + 1
        else:
            sandCoordinates[0][0] = sandCoordinates[0][0]
            sandCoordinates[0][1] = sandCoordinates[0][1] + 1
    if sandCoordinates[0][1] == maxY:
        count += 1
        break

print(len(sandCoordinates) - 1)

# Reset for part 2
maxY = maxY + 2
stoneFormation = copy.deepcopy(backupStoneFormation)
sandCoordinates = []
while(True):
    sandCoordinates.insert(0, [500,0])
    while(sandCoordinates[0][1] < maxY):
        if [sandCoordinates[0][0], sandCoordinates[0][1] + 1] in stoneFormation:
            if [sandCoordinates[0][0] - 1, sandCoordinates[0][1] + 1 ] in stoneFormation:
                if [sandCoordinates[0][0] + 1, sandCoordinates[0][1] + 1] in stoneFormation:
                    stoneFormation.append([sandCoordinates[0][0], sandCoordinates[0][1]])
                    break
                else:
                    sandCoordinates[0][0] = sandCoordinates[0][0] + 1
                    sandCoordinates[0][1] = sandCoordinates[0][1] + 1                        
            else:
                sandCoordinates[0][0] = sandCoordinates[0][0] - 1
                sandCoordinates[0][1] = sandCoordinates[0][1] + 1
        else:
            sandCoordinates[0][0] = sandCoordinates[0][0]
            sandCoordinates[0][1] = sandCoordinates[0][1] + 1
        if sandCoordinates[0][1] == maxY - 1:
            stoneFormation.append([sandCoordinates[0][0], sandCoordinates[0][1]])
            break
    if [sandCoordinates[0][0], sandCoordinates[0][1]] == [500, 0]:
        break
print(len(sandCoordinates))
 
