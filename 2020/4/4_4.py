inputArray = []

with open("input.txt") as fp:
    for line in fp:
        line = line.strip('\n')
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

count = 0

for line in inputArray:
    #variables for checks
    count += 1
    #if space (dividing the input)
    if len(line) == 0:
        #check if all of the checks are true
        if byrCheck and iyrCheck and eyrCheck and hgtCheck and hclCheck and eclCheck and pidCheck:
            print "Valid passport\n"
            totValidPassports += 1
        else:
            print "Invalid passport\n"
        
        #make all checks false here
        byrCheck = False
        iyrCheck = False
        eyrCheck = False
        hgtCheck = False
        hclCheck = False
        eclCheck = False
        pidCheck = False
        cidCheck = False
    else:
        #split the line by space (divide up all the data points)
        splitLine = line.split(" ")
        numDataPoints = len(splitLine)
        for data in splitLine:
            print data
            splitData = data.split(":")
            field = splitData[1]
            fieldLen = len(field)
            if splitData[0] == "byr":
                if fieldLen == 4 and int(field) >= 1920 and int(field) <= 2002:
                    print "byr True"
                    byrCheck = True
            elif splitData[0] == "iyr":
                if fieldLen == 4 and int(field) >= 2010 and int(field) <= 2020:
                    print "iyr True"
                    iyrCheck = True
            elif splitData[0] == "eyr":
                if fieldLen == 4 and int(field) >= 2020 and int(field) <= 2030:
                    print "eyr True"
                    eyrCheck = True
            elif splitData[0] == "hgt":
                if field[fieldLen - 2] == 'c' and field[fieldLen - 1] == 'm':
                    number = field.split("cm")
                    if int(number[0]) >= 150 and int(number[0]) <= 193:
                        print "hgt True"
                        hgtCheck = True
                elif field[fieldLen - 2] == 'i' and field[fieldLen - 1] == 'n':
                    number = field.split("in")
                    if int(number[0]) >= 59 and int(number[0]) <= 76:
                        print "hgt True"
                        hgtCheck = True
            elif splitData[0] == "hcl":
                if field[0] == '#':
                    value = ""
                    validInput = "0123456789abcdef"
                    print "hcl True"
                    if len(field) == 7:
                        validInputCheck = True
                        for i in range(1, fieldLen):
                            if field[i] not in validInput:
                                validInputCheck = False
                        if validInputCheck == True:
                            hclCheck = True
            elif splitData[0] == "ecl":
                validInput = ["amb","blu","brn","gry","grn","hzl","oth"]
                if field in validInput:
                    eclCheck = True
            elif splitData[0] == "pid":
                if fieldLen == 9:
                    pidCheck = True
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
