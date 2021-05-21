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
    print("pre total: ", total)
    sum = sum + total
    nextTotal = (total//3)-2
    while nextTotal > 0:
        sum = sum + nextTotal
        nextTotal = (nextTotal//3)-2

print("answer =", sum)
