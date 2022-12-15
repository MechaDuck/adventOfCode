import copy
input = 'input.txt'
file1 = open(input, 'r')
lines = file1.readlines()

if input == 'input.txt':
    boxArrangement = [[],[],[],[],[],[],[],[],[]]
else:
    boxArrangement = [[],[],[]]
movement = []
for line in lines:
    if "move" in line:
        movement.append([int(line.split(" ")[1]), int(line.split(" ")[3])- 1 , int(line.split(" ")[5].strip()) - 1])
    else: 
        # Example Input 
        if not input == 'input.txt' and "[" in line:
            if line[1] != " ":
                boxArrangement[0].append([line[1]])
            if line[5] != " ":
                boxArrangement[1].append([line[5]])
            if line[9] != " ":
                boxArrangement[2].append([line[9]])
        else:
            if "[" in line:
                if line[1] != " ":
                    boxArrangement[0].append([line[1]])
                if line[5] != " ":
                    boxArrangement[1].append([line[5]])
                if line[9] != " ":
                    boxArrangement[2].append([line[9]])               
                if line[13] != " ":
                    boxArrangement[3].append([line[13]])
                if line[17] != " ":
                    boxArrangement[4].append([line[17]])
                if line[21] != " ":
                    boxArrangement[5].append([line[21]])
                if line[25] != " ":
                    boxArrangement[6].append([line[25]])               
                if line[29] != " ":
                    boxArrangement[7].append([line[29]])
                if line[33] != " ":
                    boxArrangement[8].append([line[33]])

newArrangement = copy.deepcopy(boxArrangement)
for x in range(len(movement)):
    for p in range(movement[x][0]):
        newArrangement[movement[x][2]].insert(0, newArrangement[movement[x][1]].pop(0))

for i in range(len(newArrangement)):
    print(newArrangement[i][0])

newArrangementWithCraterMover9001 = copy.deepcopy(boxArrangement) 
for x in range(len(movement)):
    bunchOfCrates = []
    for p in range(movement[x][0]):
        bunchOfCrates.append(newArrangementWithCraterMover9001[movement[x][1]].pop(0))
    for q in reversed(range(len(bunchOfCrates ))):
        newArrangementWithCraterMover9001[movement[x][2]].insert(0, bunchOfCrates[q])

print("Part 2 Solution: \n")
for i in range(len(newArrangementWithCraterMover9001)):
    print(newArrangementWithCraterMover9001[i][0])        
    