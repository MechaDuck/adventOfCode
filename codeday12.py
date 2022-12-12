# if 'A' < 'B':
#     True
# print(chr((ord('b') + 1)))
# if 'z' < 'b':
#     False


class HikingMachine:
    def __init__(self, mazeList) -> None:
        self.mazeList = mazeList
        self.lengthXAxis = len(mazeList[0])
        self.lengthYAxis = len(mazeList)
        self.stepList = []
        self.foundPaths = []

    def findNextLocation(self, currX: int, currY: int, visitedArr=[], pathArr=[]):
        currVisitedArr = visitedArr[:]
        currPathArr = pathArr[:]
        if mazeList[currY][currX] == "S":
            currVisitedArr.append([currX, currY])
            currPathArr.append([currX, currY])

        nextXY = [[currX, currY + 1], [currX, currY - 1],
                  [currX + 1, currY], [currX - 1, currY]]
        for i in range(len(nextXY)):
            nextX = nextXY[i][0]
            nextY = nextXY[i][1]
            if nextY >= self.lengthYAxis or nextY < 0 or nextX >= self.lengthXAxis or nextX < 0:
                continue
            else:
                if (mazeList[currY][currX] == "z" or mazeList[currY][currX] == "y") and mazeList[nextY][nextX] == "E":
                    self.foundPaths.append(pathArr)
                if mazeList[currY][currX] == "S" and mazeList[nextY][nextX] == "a":
                    copyVisitedArr = currVisitedArr[:]
                    copyVisitedArr.append([nextX, nextY])
                    copyPathArr = currPathArr[:]
                    copyPathArr.append([nextX, nextY])
                    self.findNextLocation(
                        nextX, nextY, copyVisitedArr, copyPathArr)
                if mazeList[currY][currX] >= mazeList[nextY][nextX] or chr(ord(mazeList[currY][currX]) + 1) == mazeList[nextY][nextX]:
                    if [nextX, nextY] in visitedArr:
                        continue
                    else:
                        copyVisitedArr = currVisitedArr[:]
                        copyVisitedArr.append([nextX, nextY])
                        copyPathArr = currPathArr[:]
                        copyPathArr.append([nextX, nextY])
                        self.findNextLocation(
                            nextX, nextY, copyVisitedArr, copyPathArr)

    def getShortestPath(self):
        max = len(self.foundPaths[0])
        for i in range(len(self.foundPaths)):
            if max > len(self.foundPaths[i]):
                max = len(self.foundPaths[i])
        return max


def parseInput():
    mazeList = []
    file1 = open('input.txt', 'r')
    Lines = file1.readlines()
    for line in Lines:
        line = line.strip()
        mazeList.append(list(line))
    return mazeList


mazeList = parseInput()
myHikingMachine = HikingMachine(mazeList)
myHikingMachine.findNextLocation(0, 0)
print(myHikingMachine.getShortestPath())
