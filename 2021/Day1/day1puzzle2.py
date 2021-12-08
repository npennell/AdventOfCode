inputNumArray = []
current = None
numberLarger = 0
with open("input.txt") as input:
    for line in input:
        line = line.strip('\n')
        line = line.strip('\t')
        line = int(line)
        inputNumArray.append(line)

arrayLen = len(inputNumArray)
for i in range (0, arrayLen - 2):
    total = inputNumArray[i] + inputNumArray[i + 1] + inputNumArray[i + 2]
    if current != None:
        if total > current:
            numberLarger += 1
    current = total

print(numberLarger)
