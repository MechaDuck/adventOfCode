import numpy as np
import os
from enum import Enum

class postition(Enum):
    left = "left"
    right = "right"
    top = "top"
    bottom = "bottom"

class Tree:
    def __init__(self, height, marker: bool = False) -> None:
        self.height: int = height
        self.marker: bool = marker
    def markTree(self):
         self.marker = True
    def getHeight(self):
        return self.height
class Forest:
    def __init__(self,maxSizeX,maxSizeY) -> None:
        self.forest: Tree[int][int] = [[0 for _ in range(maxSizeX)] for _ in range(maxSizeY)]
    def plantTree(self,tree: Tree, posX: int, posY: int):
        self.forest[posX][posY] = tree
    def printForest(self):
        print(np.matrix(self.forest))

class ParserToForest:
    def __init__(self, filename: str) -> None:
        self.filename = filename
    def getForest(self):
        row: int = 0
        col: int = 0
        forest: Forest = Forest(6,6)
        with open(self.filename) as fileobj:
            for line in fileobj:
                for ch in line: 
                    forest.plantTree(Tree(ch),col,row)
                    col += 1
                row += 1
                col = 0
        return forest

class Lookout:
    def __init__(self, forest: Forest, pos: postition) -> None:
        self.forest = forest.forest
        self.pos = pos

    def getObservableTrees(self):
        highestMeasure: int = -1
        for x in range(len(self.forest[0])):
            if int(self.forest[x][0].getHeight()) > highestMeasure:
                highestMeasure = int(self.forest[x][0].getHeight())
                print(highestMeasure)


def test():
    unoTree = Tree(1)
    dosTree = Tree(2)
    tresTree = Tree(3)
    quatroTree = Tree(4)
    cincoTree = Tree(5)

    myForest = Forest(10,10)
    myForest.plantTree(unoTree, 1,3)
    myForest.plantTree(dosTree, 1,5)
    myForest.plantTree(tresTree, 1,3)
    myForest.plantTree(quatroTree, 1,3)

# test()
myParser = ParserToForest("./example_input.txt")
myForest = myParser.getForest()
myForest.printForest()
myLookout = Lookout(myForest, "left")
myLookout.getObservableTrees()





