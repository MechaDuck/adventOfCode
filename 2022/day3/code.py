
file1 = open('input.txt', 'r')
lines = file1.readlines()
rucksack = []
for line in lines:
    rucksack.append(line)

sum = 0
for i in range(len(rucksack)):

    leftCompartment = rucksack[i][0 : int(len(rucksack[i]) / 2)]
    rightCompartement = rucksack[i].strip()[int(len(rucksack[i]) / 2) : len(rucksack[i])]
    elementFound = False
    for p in range(len(leftCompartment)):
        for q in range(len(rightCompartement)):
            if leftCompartment[p] == rightCompartement[q]:
                print("Found element: ", leftCompartment[p])
                if leftCompartment[p].isupper():
                    sum += ord(leftCompartment[p]) - 38
                else:
                    sum += ord(leftCompartment[p]) - 96
                elementFound = True
                break
        if elementFound:
            break
sum = 0
elementFound = False
for i in range(0, len(rucksack), 3):
    elementFound = False
    for u in range(len(rucksack[i])):
        if elementFound:
            break
        for w in range(len(rucksack[i + 1])):
            if elementFound:
                break
            for t in range(len(rucksack[i + 2])):
                if rucksack[i][u] == rucksack[i + 1][w] and rucksack[i][u] == rucksack[i + 2][t]:
                    print(rucksack[i][u])
                    if rucksack[i][u].isupper():
                        sum += ord(rucksack[i][u]) - 38
                    else:
                        sum += ord(rucksack[i][u]) - 96
                    elementFound = True
                    break
                
print(sum)
