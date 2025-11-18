def pairedSelectionSort(idArr, numArr):
    for i in range(len(numArr)-1):
        maxIndex = i
        for j in range(i+1, len(numArr)):
            if numArr[j] >= numArr[maxIndex]:
                if numArr[j] == numArr[maxIndex]:
                    if idArr[j] < idArr[maxIndex]:
                        maxIndex = j
                else:
                    maxIndex = j
        numArr[maxIndex], numArr[i] = numArr[i], numArr[maxIndex]
        idArr[maxIndex], idArr[i] = idArr[i], idArr[maxIndex]


in_file = open("input3.txt")
out_file = open("output3.txt", "w")

t = int(in_file.readline())
idArr = in_file.readline().split()
numArr = in_file.readline().split()
for i in range(t):
    idArr[i] = int(idArr[i])
    numArr[i] = int(numArr[i])

pairedSelectionSort(idArr, numArr)

for i in range(t):
    out_file.write(f"ID: {idArr[i]} Mark: {numArr[i]}\n")

in_file.close()
out_file.close()