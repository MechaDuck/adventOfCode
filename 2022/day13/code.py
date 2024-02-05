import ast
inputs = []
file1 = open('input.txt', 'r')
Lines = file1.readlines()
for line in Lines:
    line = line.strip()
    if line != "":
        inputs.append(ast.literal_eval(line))


class ListCompare:
    def __init__(self) -> None:
        self.resultFound = None
    def compareLists(self, leftList, rightList):
        print("Compare: ", leftList, " and ", rightList)
        for x in range(len(leftList)):
            if x >= len(rightList):
                print("Right side run out of items, not in order!")
                self.resultFound = False
            if self.resultFound != None:
                return
            if not isinstance(leftList[x], list):
                if not isinstance(rightList[x], list):
                    self.compareIntegers(leftList[x], rightList[x])
                else:
                    self.compareLists([leftList[x]], rightList[x])
            else:
                if not isinstance(rightList[x], list):
                    self.compareLists(leftList[x], [rightList[x]])
                else:
                    self.compareLists(leftList[x], rightList[x])
            if self.resultFound != None:
                return
        if  len(rightList) == len(leftList):
            return
        print("left side run out or items first")
        self.resultFound = True
        return

    def compareIntegers(self, leftInt, rightInt):
        print("Compare: " ,leftInt, " and ", rightInt)
        if leftInt == rightInt:
            return
        if leftInt < rightInt:
            print("left side is smaller, so inputs are in the right order")
            self.resultFound = True
            return
        print("right side is smaller, so inputs are not in the right order")
        self.resultFound = False
        return

def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            myCompare = ListCompare()
            myCompare.compareLists(inputs[j + 1], inputs[j])
            if myCompare.resultFound:            
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return

def getPacketIndexFromMarker(arr, marker):
    for i in range(len(arr)):
        if arr[i] == marker:
            return i + 1

def calcDecoderKey(arr, markerOne, markerTwo):
    return getPacketIndexFromMarker(arr, markerOne) * getPacketIndexFromMarker(arr, markerTwo)

count = 0
for i in range(0, len(inputs), 2):

    myCompare = ListCompare()
    myCompare.compareLists(inputs[i], inputs[i+1])
    compareResult = myCompare.resultFound

    print(compareResult)
    if compareResult:
        count += i / 2 + 1
print(count)

markerOne = [[2]]
markerTwo = [[6]]
inputs.append(markerOne)
inputs.append(markerTwo)
bubbleSort(inputs)
print(calcDecoderKey(inputs, markerOne, markerTwo))