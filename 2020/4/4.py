inputArray = []

with open("input.txt") as fp:
    for line in fp:
        #line = line.strip('\n')
        line = line.strip('\t')
        inputArray.append(line)

fp.close()

totValidPassports = 0

byrCheck = False
iyrCheck = False
eyrCheck = False
hgtCheck = False
hclCheck = False
eclCheck = False
pidCheck = False
cidCheck = False
isValid = False
linesInFile = len(inputArray)
print linesInFile
count = 0

for line in inputArray:
    #variables for checks
    count += 1
    print count
    #if space (dividing the input)
    if line == "\n":
        #check if all of the checks are true
        if byrCheck and iyrCheck and eyrCheck and hgtCheck and hclCheck and eclCheck and pidCheck and cidCheck == True:
            print "Valid passport"
            totValidPassports += 1
        elif (byrCheck and iyrCheck and eyrCheck and hgtCheck and hclCheck and eclCheck and pidCheck == True) and cidCheck == False:
            print "Valid passport"
            totValidPassports += 1
        else:
            print "Invalid passport"
        
        #make all checks false here
        byrCheck = False
        iyrCheck = False
        eyrCheck = False
        hgtCheck = False
        hclCheck = False
        eclCheck = False
        pidCheck = False
        cidCheck = False
   
    #split the line by space (divide up all the data points)
    splitLine = line.split(" ")
    numDataPoints = len(splitLine)
    for data in splitLine:
        print data
        splitData = data.split(":")
        print splitData
        if splitData[0] == "byr":
            byrCheck = True
        elif splitData[0] == "iyr":
            iyrCheck = True
        elif splitData[0] == "eyr":
            eyrCheck = True
        elif splitData[0] == "hgt":
            hgtCheck = True
        elif splitData[0] == "hcl":
            hclCheck = True
        elif splitData[0] == "ecl":
            eclCheck = True
        elif splitData[0] == "pid":
            pidCheck = True
        elif splitData[0] == "cid":
            cidCheck = True
    if count == linesInFile:
        if byrCheck and iyrCheck and eyrCheck and hgtCheck and hclCheck and eclCheck and pidCheck and cidCheck == True:
            print "Valid passport"
            totValidPassports += 1
        elif (byrCheck and iyrCheck and eyrCheck and hgtCheck and hclCheck and eclCheck and pidCheck == True) and cidCheck == False:
            print "Valid passport"
            totValidPassports += 1
        else:
            print "Invalid passport"
        
        #make all checks false here
        byrCheck = False
        iyrCheck = False
        eyrCheck = False
        hgtCheck = False
        hclCheck = False
        eclCheck = False
        pidCheck = False
        cidCheck = False

print("Total valid passports: ", totValidPassports)
