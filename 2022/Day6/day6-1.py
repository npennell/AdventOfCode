import utilFile

# store input
path = '../AdventOfCode/2022/Data/inputDay6.txt'
inputArray = utilFile.storeInput(path)

firstInput = inputArray[0]

result = None
letters = []
stringIndexCount = 0

# for every charavter
for char in firstInput:
    if char not in letters:
        # add in letter if not at 4 characters
        if len(letters) < 4:
            letters.append(char)
        # at 4 letters, have result
        else:
            result = stringIndexCount
            break
    # duplicate letter
    else:
        # remove everything up to and including duplicate letter
        duplicateIndex = letters.index(char)
        for x in range(duplicateIndex + 1):
            del letters[0]
        # add in letter to end
        letters.append(char)
    # increase the current letter count
    stringIndexCount += 1            
        
print(letters)
print(result)
    