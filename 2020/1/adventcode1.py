inputNumArray = []

#store info from file

with open("inputNums.txt") as input:
    for line in input:
        line = line.strip('\n')
        line = line.strip('\t')
        line = int(line)
        inputNumArray.append(line)

fp.close()

print(inputNumArray)
print(len(inputNumArray))
#work with input
count = 0
answer = 0
#i is the starting value
for i in inputNumArray:
    count = count + 1
    for j in range(count, len(inputNumArray)):
        if i + inputNumArray[j] == 2020:
            answer = i * inputNumArray[j]

print('answer = ', answer)


