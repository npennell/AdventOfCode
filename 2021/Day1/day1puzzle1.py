current = None
numberLarger = 0
with open("input.txt") as input:
    for line in input:
        line = line.strip('\n')
        line = line.strip('\t')
        line = int(line)
        if current != None:
            if line > current:
                numberLarger += 1
        current = line

print(numberLarger)