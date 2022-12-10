from enum import Enum

class Direction(Enum):
    R = "moveRight"
    L = "moveLeft"
    U = "moveUp"
    D = "moveDown"

class Plank:
    def __init__(self) -> None:
        pass
    def setVisited(self):
        self.visited = True
    def getIsVisited(self):
        return self.visited
class CoordinatesBucket:
    def __init__(self) -> None:
        self.coordinates: int[int] = [[0,0]]
    def addNewCoordinate(self, posX, posY):
        self.coordinates.append([posX, posY])
    def getLatestCoordinate(self):
        return self.coordinates[-1]

class StateMachineKnot:
    def __init__(self) -> None:
        self.state = "H00_T00"
        self.coordinatesBucket = CoordinatesBucket()
        self.movementBucket: str[int] = []
        self.doubleMovements: int = 0
        pass
    def getMovements(self):
        return self.movementBucket
    def moveMultipleTimesInOneDirection(self, times: int, direction):
        for x in range(times):
            self.move(direction)

    def moveMultipleKnotsMultipleTimesInOneDirection(self, times: int, direction, knotCount):
        for x in range(times):
            self.move(direction)

    def moveOnce(self, complexDirection):
        if complexDirection == "LU":
            self.move("L")
            self.move("U")
        elif complexDirection == "LD":
            self.move("L")
            self.move("D")
        elif complexDirection == "RD":
            self.move("R")
            self.move("D")
        elif complexDirection == "UR":
            self.move("U")
            self.move("R")
        else:
            self.move(complexDirection)

    def getCountOfDifferentCoordinates(self):
        newlist = []
        for i in self.coordinatesBucket.coordinates:
            if i not in newlist:
                newlist.append(i)
        return len(newlist)

    def move(self, nextDirection):
        currPos = self.coordinatesBucket.getLatestCoordinate()
        currPosX = currPos[0]
        currPosY = currPos[1]
        match self.state:
            case "H00_T00":
                if nextDirection == "R":
                    self.state = "H10_T00"
                    return
                if nextDirection == "L":
                    self.state = "H00_T10"
                    return
                if nextDirection == "U":
                    self.state = "H01_T00"
                    return
                if nextDirection == "D":
                    self.state = "H00_T01"
                    return
                if nextDirection == "LU":
                    self.state = "H01_T10"
                    return
                if nextDirection == "LD":
                    self.state = "H00_T11"
                    return
                if nextDirection == "RD":
                    self.state = "H10_T01"
                    return
                if nextDirection == "UR":
                    self.state = "H11_T00"
                    return
            case "H10_T00":
                if nextDirection == "R":
                    self.state = "H10_T00"
                    self.coordinatesBucket.addNewCoordinate(currPosX + 1, currPosY)
                    self.movementBucket.append("R")
                    return 
                if nextDirection == "L":
                    self.state = "H00_T00"
                    return
                if nextDirection == "U":
                    self.state = "H11_T00"
                    return
                if nextDirection == "D":
                    self.state = "H10_T01"
                    return
                if nextDirection == "LU":
                    self.state = "H01_T00"
                    return
                if nextDirection == "LD":
                    self.state = "H00_T01"
                    return
                if nextDirection == "RD":
                    self.state = "H10_T00"
                    self.coordinatesBucket.addNewCoordinate(currPosX + 1, currPosY - 1)
                    self.movementBucket.append("RD")
                    return
                if nextDirection == "UR":
                    self.state = "H10_T00"
                    self.coordinatesBucket.addNewCoordinate(currPosX + 1, currPosY + 1)
                    self.movementBucket.append("UR")
                    return
            case "H01_T00":
                if nextDirection == "R":
                    self.state = "H11_T00"
                    return
                if nextDirection == "L":
                    self.state = "H01_T10"
                    return
                if nextDirection == "U":
                    self.state = "H01_T00"
                    self.coordinatesBucket.addNewCoordinate(currPosX, currPosY + 1)
                    self.movementBucket.append("U")
                    return
                if nextDirection == "D":
                    self.state = "H00_T00"
                    return
                if nextDirection == "LU":
                    self.state = "H01_T00"
                    self.coordinatesBucket.addNewCoordinate(currPosX - 1, currPosY + 1)
                    self.movementBucket.append("LU")
                    return
                if nextDirection == "LD":
                    self.state = "H00_T10"
                    return
                if nextDirection == "RD":
                    self.state = "H10_T00"
                    return
                if nextDirection == "UR":
                    self.state = "H01_T00"
                    self.coordinatesBucket.addNewCoordinate(currPosX + 1, currPosY + 1)
                    self.movementBucket.append("UR")
                    return 
            case "H00_T01":
                if nextDirection == "R":
                   self.state = "H10_T01" 
                   return 
                if nextDirection == "L":
                    self.state = "H00_T11"
                    return 
                if nextDirection == "U":
                    self.state = "H00_T00"
                    return 
                if nextDirection == "D":
                    self.state = "H00_T01"
                    self.coordinatesBucket.addNewCoordinate(currPosX, currPosY - 1)
                    self.movementBucket.append("D")
                    return 
                if nextDirection == "LU":
                    self.state = "H00_T10"
                    return
                if nextDirection == "LD":
                    self.state = "H00_T01"
                    self.coordinatesBucket.addNewCoordinate(currPosX - 1, currPosY - 1)
                    self.movementBucket.append("LD")
                    return
                if nextDirection == "RD":
                    self.state = "H00_T01"
                    self.coordinatesBucket.addNewCoordinate(currPosX + 1, currPosY - 1)
                    self.movementBucket.append("RD")
                    return
                if nextDirection == "UR":
                    self.state = "H10_T00"
                    return
            case "H01_T10":
                if nextDirection == "R":
                    self.state = "H01_T00" 
                    return
                if nextDirection == "L":
                    self.state = "H00_T10" 
                    self.coordinatesBucket.addNewCoordinate(currPosX - 1, currPosY + 1)
                    self.movementBucket.append("LU")
                    return
                if nextDirection == "U":
                    self.state = "H01_T00" 
                    self.coordinatesBucket.addNewCoordinate(currPosX - 1, currPosY + 1)
                    self.movementBucket.append("LU")
                    return
                if nextDirection == "D":
                    self.state = "H00_T10" 
                    return
                if nextDirection == "LU":
                    self.state = "H01_T10"
                    self.coordinatesBucket.addNewCoordinate(currPosX - 1, currPosY + 1)
                    self.movementBucket.append("LU")
                    return
                if nextDirection == "LD":
                    self.state = "H00_T10"
                    self.coordinatesBucket.addNewCoordinate(currPosX - 1, currPosY)
                    self.movementBucket.append("L")
                    return
                if nextDirection == "RD":
                    self.state = "H00_T00"
                    return
                if nextDirection == "UR":
                    self.state = "H01_T00"
                    self.coordinatesBucket.addNewCoordinate(currPosX, currPosY + 1)
                    self.movementBucket.append("U")
                    return
            case "H00_T10":
                if nextDirection == "R":
                    self.state = "H00_T00" 
                    return
                if nextDirection == "L":
                    self.state = "H00_T10" 
                    self.coordinatesBucket.addNewCoordinate(currPosX - 1, currPosY)
                    self.movementBucket.append("L")                    
                    return
                if nextDirection == "U":
                    self.state = "H01_T10" 
                    return
                if nextDirection == "D":
                    self.state = "H00_T11" 
                    return
                if nextDirection == "LU":
                    self.state = "H01_T10"
                    self.coordinatesBucket.addNewCoordinate(currPosX - 1, currPosY + 1)
                    self.movementBucket.append("LU")
                    return
                if nextDirection == "LD":
                    self.state = "H00_T10"
                    self.coordinatesBucket.addNewCoordinate(currPosX - 1, currPosY - 1)
                    self.movementBucket.append("LD")
                    return
                if nextDirection == "RD":
                    self.state = "H00_T01"
                    return
                if nextDirection == "UR":
                    self.state = "H01_T00"
                    return
            case "H00_T11":
                if nextDirection == "R":
                    self.state = "H00_T01" 
                    return
                if nextDirection == "L":
                    self.state = "H00_T10" 
                    self.coordinatesBucket.addNewCoordinate(currPosX - 1, currPosY - 1)
                    self.movementBucket.append("LD")
                    return
                if nextDirection == "U":
                    self.state = "H00_T10" 
                    return
                if nextDirection == "D":
                    self.state = "H00_T01" 
                    self.coordinatesBucket.addNewCoordinate(currPosX - 1, currPosY - 1)
                    self.movementBucket.append("LD")
                    return
                if nextDirection == "LU":
                    self.state = "H00_T10"
                    self.coordinatesBucket.addNewCoordinate(currPosX - 1, currPosY)
                    self.movementBucket.append("L")
                    return
                if nextDirection == "LD":
                    self.state = "H00_T11"
                    self.coordinatesBucket.addNewCoordinate(currPosX - 1, currPosY - 1)
                    self.movementBucket.append("LD")
                    return
                if nextDirection == "RD":
                    self.state = "H00_T01"
                    self.coordinatesBucket.addNewCoordinate(currPosX, currPosY - 1)
                    self.movementBucket.append("D")
                    return
                if nextDirection == "UR":
                    self.state = "H00_T00"
                    return
            case "H10_T01":
                if nextDirection == "R":
                    self.state = "H10_T00" 
                    self.coordinatesBucket.addNewCoordinate(currPosX + 1, currPosY - 1)
                    self.movementBucket.append("RD")
                    return
                if nextDirection == "L":
                    self.state = "H00_T01" 
                    return
                if nextDirection == "U":
                    self.state = "H10_T00" 
                    return
                if nextDirection == "D":
                    self.state = "H00_T01" 
                    self.coordinatesBucket.addNewCoordinate(currPosX + 1, currPosY - 1)
                    self.movementBucket.append("RD")
                    return
                if nextDirection == "LU":
                    self.state = "H00_T00"
                    return
                if nextDirection == "LD":
                    self.state = "H00_T01"
                    self.coordinatesBucket.addNewCoordinate(currPosX, currPosY - 1)
                    self.movementBucket.append("D")
                    return
                if nextDirection == "RD":
                    self.state = "H10_T01"
                    self.coordinatesBucket.addNewCoordinate(currPosX + 1, currPosY - 1)
                    self.movementBucket.append("RD")
                    return
                if nextDirection == "UR":
                    self.state = "H10_T00"
                    self.coordinatesBucket.addNewCoordinate(currPosX + 1, currPosY)
                    self.movementBucket.append("R")
                    return
            case "H11_T00":
                if nextDirection == "R":
                    self.state = "H10_T00" 
                    self.coordinatesBucket.addNewCoordinate(currPosX + 1, currPosY + 1)
                    self.movementBucket.append("UR")
                    return
                if nextDirection == "L":
                    self.state = "H01_T00" 
                    return
                if nextDirection == "U":
                    self.state = "H01_T00" 
                    self.coordinatesBucket.addNewCoordinate(currPosX + 1, currPosY + 1)
                    self.movementBucket.append("UR")
                    return
                if nextDirection == "D":
                    self.state = "H10_T00"
                    return
                if nextDirection == "LU":
                    self.state = "H01_T00"
                    self.coordinatesBucket.addNewCoordinate(currPosX, currPosY + 1)
                    self.movementBucket.append("U")
                    return
                if nextDirection == "LD":
                    self.state = "H00_T00"
                    return
                if nextDirection == "RD":
                    self.state = "H10_T00"
                    self.coordinatesBucket.addNewCoordinate(currPosX + 1, currPosY)
                    self.movementBucket.append("R")
                    return
                if nextDirection == "UR":
                    self.state = "H11_T00"
                    self.coordinatesBucket.addNewCoordinate(currPosX + 1, currPosY + 1)
                    self.movementBucket.append("UR")
                    return

myStateMachineKnot1 = StateMachineKnot()         
myStateMachineKnot2 = StateMachineKnot()         
myStateMachineKnot3 = StateMachineKnot()         
myStateMachineKnot4 = StateMachineKnot()         
myStateMachineKnot5 = StateMachineKnot()         
myStateMachineKnot6 = StateMachineKnot()   
myStateMachineKnot7 = StateMachineKnot()   
myStateMachineKnot8 = StateMachineKnot()   
myStateMachineKnot9 = StateMachineKnot()  
myStateMachineKnot10 = StateMachineKnot()  
file1 = open('input.txt', 'r')
Lines = file1.readlines()
for line in Lines:
    direction = line.split(" ")[0]
    times = int(line.split(" ")[1].strip())
    myStateMachineKnot1.moveMultipleTimesInOneDirection(times, direction)

print(myStateMachineKnot1.getCountOfDifferentCoordinates())

movements = myStateMachineKnot1.getMovements()
for x in movements:
    myStateMachineKnot2.move(x)

movements = myStateMachineKnot2.getMovements()
for x in movements:
    myStateMachineKnot3.move(x)

movements = myStateMachineKnot3.getMovements()
for x in movements:
    myStateMachineKnot4.move(x)

movements = myStateMachineKnot4.getMovements()
for x in movements:
    myStateMachineKnot5.move(x)

movements = myStateMachineKnot5.getMovements()
for x in movements:
    myStateMachineKnot6.move(x)

movements = myStateMachineKnot6.getMovements()
for x in movements:
    myStateMachineKnot7.move(x)

movements = myStateMachineKnot7.getMovements()
for x in movements:
    myStateMachineKnot8.move(x)

movements = myStateMachineKnot8.getMovements()
for x in movements:
    myStateMachineKnot9.move(x)

print(myStateMachineKnot9.getCountOfDifferentCoordinates())
