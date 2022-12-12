inputArray = []

def storeInput(path):
    with open(path) as input:
        for line in input:
            line = line.strip('\n')
            line = line.strip('\t')
            inputArray.append(line)
    return inputArray