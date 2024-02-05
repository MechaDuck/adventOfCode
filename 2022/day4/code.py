file1 = open('input.txt', 'r')
lines = file1.readlines()
elveSections = []
for line in lines:
    elveSections.append([line.split(",")[0], line.split(",")[1].strip()])

sum = 0
for x in range(len(elveSections)):
    startLeft = int(elveSections[x][0].split("-")[0])
    endLeft = int(elveSections[x][0].split("-")[1].strip())

    startRight = int(elveSections[x][1].split("-")[0])
    endRight = int(elveSections[x][1].split("-")[1])

    if startLeft >= startRight and endLeft <= endRight:
        print("Found match in ", elveSections[x])
        sum += 1
    elif startRight >= startLeft and endRight <= endLeft:
        print("Found match in ", elveSections[x])
        sum += 1

print(sum)

# Part 2
sum = 0
for x in range(len(elveSections)):
    startLeft = int(elveSections[x][0].split("-")[0])
    endLeft = int(elveSections[x][0].split("-")[1].strip())

    startRight = int(elveSections[x][1].split("-")[0])
    endRight = int(elveSections[x][1].split("-")[1])

    if startLeft <= endRight and startLeft >= startRight:
        print("Found match in ", elveSections[x])
        sum += 1
    elif startRight <= endLeft and startRight >= startLeft:
        print("Found match in ", elveSections[x])
        sum += 1

print(sum)