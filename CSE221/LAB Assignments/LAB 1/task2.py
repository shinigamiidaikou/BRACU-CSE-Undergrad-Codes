def bubbleSort(arr):
    count = 0   # Sorted bubble counter
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                # counting how many bubbles are already ordered ascendingly
                count+=1
        # if all numbers are ordered, 
        # counter will be 1 less than length
        if count == len(arr) - 1:
            break

in_file = open("input2.txt")
out_file = open("output2.txt", "w")

t = int(in_file.readline())
arr = in_file.readline().split()
for i in range(t):
    arr[i] = int(arr[i])

bubbleSort(arr)

out_file.write(str(arr[0]))
for i in range(1,t):
    out_file.write(" "+str(arr[i]))

in_file.close()
out_file.close()