import numpy as np

class Tree:
    def __init__(self, height, marker: bool = False) -> None:
        self.height: int = height
        self.marker: bool = marker
    def setMark(self):
         self.marker = True
    def getHeight(self):
        return self.height
    def getIsMarked(self):
        return self.marker
    def setScenicScore(self, score):
        self.scenicScore = score
    def getScenicScore(self):
        return self.scenicScore
class Forest:
    def __init__(self, maxSizeX, maxSizeY) -> None:
        self.forest: Tree[int][int] = [[0 for _ in range(maxSizeX)] for _ in range(maxSizeY)]
    def plantTree(self,tree: Tree, posX: int, posY: int):
        self.forest[posX][posY] = tree
    def printForest(self):
        print(np.matrix(self.forest))
    def countMarkedTrees(self):
        counter: int = 0
        for y in range(len(self.forest)):
            for x in range(len(self.forest[0])):
                if self.forest[x][y].getIsMarked():
                    counter += 1
        return counter

class ParserToForest:
    def __init__(self, filename: str) -> None:
        self.filename = filename
    def getForest(self):
        row: int = 0
        col: int = 0
        self.getForestSize()
        forest: Forest = Forest(self.maxX,self.maxY)
        with open(self.filename) as fileobj:
            for line in fileobj:
                for ch in line: 
                    if ch == "\n":
                        break
                    forest.plantTree(Tree(ch),col,row)
                    col += 1
                row += 1
                col = 0
        return forest
    def getForestSize(self):
        with open(self.filename) as fileobj:
            line = fileobj.readline()
            counter: int = 0
            for ch in line:
                if ch == "\n":
                    break
                counter += 1    
            self.maxY = counter
            self.maxX = 1 + sum(1 for line in fileobj)



class LookoutPosition:
    def __init__(self, forest: Forest) -> None:
        self.forest = forest.forest

    def getObservableTrees(self):
        highestMeasure: int = -1
        # left to right
        for y in range(len(self.forest)):
            for x in range(len(self.forest[0])):
                if int(self.forest[x][y].getHeight()) > highestMeasure:
                    highestMeasure = int(self.forest[x][y].getHeight())
                    self.forest[x][y].setMark()
            highestMeasure = -1
        # top to bottom
        for x in range(len(self.forest[0])):
            for y in range(len(self.forest)):
                if int(self.forest[x][y].getHeight()) > highestMeasure:
                    highestMeasure = int(self.forest[x][y].getHeight())
                    self.forest[x][y].setMark()
            highestMeasure = -1
        # right to left
        for y in range(len(self.forest)):
            for x in reversed(range(len(self.forest[0]))):
                if int(self.forest[x][y].getHeight()) > highestMeasure:
                    highestMeasure = int(self.forest[x][y].getHeight())
                    self.forest[x][y].setMark()
            highestMeasure = -1          
        # bottom to top
        for x in reversed(range(len(self.forest[0]))):
            for y in reversed(range(len(self.forest))):
                if int(self.forest[x][y].getHeight()) > highestMeasure:
                    highestMeasure = int(self.forest[x][y].getHeight())
                    self.forest[x][y].setMark()
            highestMeasure = -1       

    def calculateScenicScoresForTrees(self):
        for x in range(len(self.forest[0])):
            for y in range(len(self.forest)):
                scenicScoreLeftToRight: int = 0
                # scenic score left to right
                # check index does not exceed
                if x + 1 < len(self.forest[0]):
                    highestMeasure = int(self.forest[x][y].getHeight())
                    for xScenic in range(x + 1, len(self.forest[0])):
                        if int(self.forest[xScenic][y].getHeight()) < highestMeasure:
                            scenicScoreLeftToRight += 1
                        else:
                            scenicScoreLeftToRight += 1   
                            break
                # scenic score top to bottom
                scenicScoreTopToBottom = 0
                # check index does not exceed
                if y + 1 < len(self.forest):
                    highestMeasure = int(self.forest[x][y].getHeight())
                    for yScenic in range(y + 1, len(self.forest)):
                        if int(self.forest[x][yScenic].getHeight()) < highestMeasure:
                            scenicScoreTopToBottom += 1
                        else:
                            scenicScoreTopToBottom += 1 
                            break
                # scenic score right to left    
                scenicScoreRightToLeft = 0

                highestMeasure = int(self.forest[x][y].getHeight())
                for xScenicRev in reversed(range(x)):
                    if int(self.forest[xScenicRev][y].getHeight()) < highestMeasure:
                        scenicScoreRightToLeft += 1
                    else:
                        scenicScoreRightToLeft += 1
                        break   
                # scenic score bottom to top    
                scenicScoreBottomToTop = 0

                highestMeasure = int(self.forest[x][y].getHeight())
                for yScenicRev in reversed(range(y)):
                    if int(self.forest[x][yScenicRev].getHeight()) < highestMeasure:
                        scenicScoreBottomToTop += 1
                    else:
                        scenicScoreBottomToTop += 1
                        break                       
                self.forest[x][y].setScenicScore(scenicScoreLeftToRight * scenicScoreTopToBottom * scenicScoreRightToLeft * scenicScoreBottomToTop)

    def findTreeIfHighestScenicScore(self):
        self.calculateScenicScoresForTrees()
        highestScenicScore = self.forest[0][0].getScenicScore()
        for x in range(len(self.forest[0])):
            for y in range(len(self.forest)):
                if self.forest[x][y].getScenicScore() > highestScenicScore:
                    highestScenicScore = self.forest[x][y].getScenicScore()
        return highestScenicScore

                                        
         

myParser = ParserToForest("./input.txt")
myForest = myParser.getForest()
#myForest.printForest()
myLookout = LookoutPosition(myForest)
myLookout.getObservableTrees()
print(myForest.countMarkedTrees())
print(myLookout.findTreeIfHighestScenicScore())





