def parseInput():
    mazeList = []
    file1 = open('example_input.txt', 'r')
    Lines = file1.readlines()
    for line in Lines:
        line = line.strip()
        mazeList.append(list(line))
    return mazeList


mazeList = parseInput()
myHikingMachine = HikingMachine(mazeList)
myHikingMachine.findNextLocation(0, 0)
print(myHikingMachine.getShortestPath())
