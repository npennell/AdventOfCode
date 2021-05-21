inputArray = []

with open("input.txt") as fp:
    for line in fp:
        line = line.strip('\n')
        line = line.strip('\t')
        inputArray.append(line)

fp.close()

treeCount = 0
indexNum = 0
threeCount = 0
lineLen = 0
currentLine = 0
lineCount = len(inputArray)


lineLen = len(inputArray[currentLine])
#loop through all of the lines based on the slope
while currentLine < lineCount:
    #3 across check
    for i in range(3):
        indexNum += 1
        if indexNum == lineLen:
            indexNum = 0
    #go to next line
    currentLine += 1
    #tree check
    if (currentLine < lineCount):
        print(inputArray[currentLine][indexNum])
        if inputArray[currentLine][indexNum] == '#':
            treeCount += 1
        lineLen = len(inputArray[currentLine])

print("Number of trees for 3, 1 is: ", treeCount)


