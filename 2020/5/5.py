inputArray = []

with open("input.txt") as fp:
    for line in fp:
        line = line.strip('\n')
        line = line.strip('\t')
        inputArray.append(line)

fp.close()

highestSeatID = 0
rowNum = ""
columnNum = ""


#testing for whole data set
for data in inputArray:
    rowKey = ""
    columnKey = ""
    minRow = 0
    maxRow = 127
    rowDiff = 128
    rowNum = 0
    columnNum = 0
    minColumn = 0
    maxColumn = 7
    columnDiff = 8
    seatNum = 0
    
    print data
    for i in range(0, 7):
        rowKey += data[i]
    for j in range(7, 10):
        columnKey += data[j]
    print rowNum
    print columnNum
    print

    #figure out row #
    for i in rowKey:
        if rowDiff == 2:
            if i == 'F':
                rowNum = minRow
            else:
                rowNum = maxRow
        else:
            if i == 'F':
                #lower half, minRow doesnt change, maxRow = half of rowDiff - 1
                maxRow =  maxRow - (rowDiff / 2)
            else: #B
                #upper half, maxRow doesnt change, minRow = half rowDiff
                minRow = minRow + (rowDiff / 2)
            #calc rowDiff
            rowDiff /= 2
    print rowNum

    for j in columnKey:
        print j
        if columnDiff == 2:
            if j == 'R':
                columnNum = maxColumn
            else:
                columnNum = minColumn
        else:
            if j == 'R':
                minColumn = minColumn + (columnDiff / 2)
            else:
                maxColumn = maxColumn - (columnDiff / 2)

        columnDiff /= 2
    print columnNum

    seatNum = (rowNum * 8) + columnNum
    if seatNum > highestSeatID:
        highestSeatID = seatNum

print "highest seat number = ", highestSeatID


