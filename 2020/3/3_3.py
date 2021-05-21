inputArray = []

with open("input.txt") as fp:
    for line in fp:
        line = line.strip('\n')
        line = line.strip('\t')
        inputArray.append(line)

fp.close()

treeCount = 0
totTreeCount = 0
indexNum = 0
threeCount = 0
lineLen = 0
currentLine = 0
lineCount = len(inputArray)
slopeArray = [[1,1],[3,1],[5,1],[7,1],[1,2]]


lineLen = len(inputArray[currentLine])
#loop through all of the lines based on the slope
for j in slopeArray:
    treeCount = 0
    indexNum = 0
    threeCount = 0
    lineLen = 0
    currentLine = 0
    lineCount = len(inputArray)
    while currentLine < lineCount:
        #3 across check
        slope1 = j[0]
        for i in range(slope1):
            indexNum += 1
            if indexNum == lineLen:
                indexNum = 0
        #go to next line
        slope2 = j[1]
        currentLine += slope2
        #tree check
        if (currentLine < lineCount):
            print(inputArray[currentLine][indexNum])
            if inputArray[currentLine][indexNum] == '#':
                treeCount += 1
            lineLen = len(inputArray[currentLine])

    if totTreeCount == 0:
        totTreeCount = treeCount
    else:
        totTreeCount = totTreeCount * treeCount

print("Number of trees is: ", totTreeCount)
