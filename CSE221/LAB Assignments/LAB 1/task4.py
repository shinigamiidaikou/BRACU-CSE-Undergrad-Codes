trainDetails = []

in_file = open("input4.txt")
t = int(in_file.readline())
for i in range(t):
    # 2D array creation
    trainDetails.append(in_file.readline().split())
in_file.close()

# sorting according to conditions:
for i in range(t-1):
    minIndex = i
    for j in range(i+1, t):
        if trainDetails[j][0] <= trainDetails[minIndex][0]:
            if trainDetails[j][0] == trainDetails[minIndex][0]:
                if int(trainDetails[j][6].replace(":", "")) > int(trainDetails[minIndex][6].replace(":", "")):
                    minIndex = j
            else:
                minIndex = j
    trainDetails[minIndex], trainDetails[i] = trainDetails[i], trainDetails[minIndex]


out_file = open("output4.txt", "w")
for i in range(t):
    out_file.write(" ".join(trainDetails[i])+"\n")
out_file.close()