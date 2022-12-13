from collections import deque

class Node:
    def __init__(self, xValue, yValue) -> None:
        self.xValue = xValue
        self.yValue = yValue

class Graph:  
    def __init__(self) -> None:
        self.startCoord = ()
        self.goalCoord  = ()
        self.startCoordArr = []
    def constructGraphFromMaze(self, mazeList):
        self.graphDict = {}
        # down, right, up, left
        neighbours = [[0, 1], [1,0] ,[0, -1], [-1, 0]]
        maxYLength = len(mazeList)
        maxXLength = len(mazeList[0])
        self.findStartAndEndAndReplace(mazeList)
        for y in range(maxYLength):
            for x in range(maxXLength):
                self.graphDict[(x,y)] = []
                for n in range(len(neighbours)):
                    nextNeighbourCoord = [x + neighbours[n][0], y + neighbours[n][1]]
                    if nextNeighbourCoord[0] < maxXLength and nextNeighbourCoord[1] < maxYLength and nextNeighbourCoord[0] >= 0 and nextNeighbourCoord[1] >= 0:
                        if (mazeList[y][x] >= mazeList[nextNeighbourCoord[1]][nextNeighbourCoord[0]] or 
                            chr(ord(mazeList[y][x]) + 1) == mazeList[nextNeighbourCoord[1]][nextNeighbourCoord[0]]):
                                self.graphDict[(x,y)].append((nextNeighbourCoord[0], nextNeighbourCoord[1]))
    def findStartAndEndAndReplace(self, mazeList):
        for y in range(len(mazeList)):
            for x in range(len(mazeList[0])):        
                if mazeList[y][x] == "S":
                    self.startCoord = (x, y)
                    mazeList[y][x] = "a"
                    self.startCoordArr.append((x, y))
                if mazeList[y][x] == "E":
                    self.goalCoord = (x, y)
                    mazeList[y][x] = "z"
                if mazeList[y][x] == "a":
                    self.startCoordArr.append((x, y))

def parseInput():
    mazeList = []
    file1 = open('input.txt', 'r')
    Lines = file1.readlines()
    for line in Lines:
        line = line.strip()
        mazeList.append(list(line))
    return mazeList

# Python implementation to find the
# shortest path in the graph using
# dictionaries

# Function to find the shortest
# path between two nodes of a graph
def BFS_SP(graph, start, goal):
	explored = []
	
	# Queue for traversing the
	# graph in the BFS
	queue = [[start]]
	
	# If the desired node is
	# reached
	if start == goal:
		print("Same Node")
		return
	
	# Loop to traverse the graph
	# with the help of the queue
	while queue:
		path = queue.pop(0)
		node = path[-1]
		
		# Condition to check if the
		# current node is not visited
		if node not in explored:
			neighbours = graph[node]
			
			# Loop to iterate over the
			# neighbours of the node
			for neighbour in neighbours:
				new_path = list(path)
				new_path.append(neighbour)
				queue.append(new_path)
				
				# Condition to check if the
				# neighbour node is the goal
				if neighbour == goal:
					return len(new_path) - 1
			explored.append(node)
	return



mazeList = parseInput()
myGraph = Graph()

myGraph.constructGraphFromMaze(mazeList)
print(BFS_SP(myGraph.graphDict, myGraph.startCoord, myGraph.goalCoord))


## Part 2

length = []
for q in range(len(myGraph.startCoordArr)):
    lengthPath = BFS_SP(myGraph.graphDict, myGraph.startCoordArr[q], myGraph.goalCoord) 
    if lengthPath != None:
        length.append(lengthPath)

length.sort()
print(length[0])
