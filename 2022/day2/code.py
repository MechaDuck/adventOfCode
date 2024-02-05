def calculateScore(oppenent, response):
    if oppenent == "A":
        if response == "X":
            return 4
        if response == "Y":
            return 8
        if response == "Z":
            return 3
    if oppenent == "B":
        if response == "X":
            return 1
        if response == "Y":
            return 5
        if response == "Z":
            return 9
    if oppenent == "C":
        if response == "X":
            return 7
        if response == "Y":
            return 2
        if response == "Z":
            return 6

def calculateScoreWithSecretStrategy(oppenent, response):
    if oppenent == "A":
        if response == "X":
            return 3
        if response == "Y":
            return 4
        if response == "Z":
            return 8
    if oppenent == "B":
        if response == "X":
            return 1
        if response == "Y":
            return 5
        if response == "Z":
            return 9
    if oppenent == "C":
        if response == "X":
            return 2
        if response == "Y":
            return 6
        if response == "Z":
            return 7

file1 = open('input.txt', 'r')
Lines = file1.readlines()

totalScore = 0
for line in Lines:
    oppenent = line.split(" ")[0]
    response = line.split(" ")[1].strip()
    totalScore += calculateScore(oppenent, response)

print(totalScore)

#part 2
file1.seek(0, 0)
Lines = file1.readlines()

totalScore = 0
for line in Lines:
    oppenent = line.split(" ")[0]
    response = line.split(" ")[1].strip()
    totalScore += calculateScoreWithSecretStrategy(oppenent, response)
print(totalScore)
