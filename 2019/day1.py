inputArray = []

with open("inputday1.txt") as fp:
    for line in fp:
        line = line.strip('\n')
        line = line.strip('\t')
        line = int(line)
        inputArray.append(line)

fp.close()

sum = 0

for i in inputArray:
    total = (i//3)-2
    sum = sum + total

print("answer =", sum)

