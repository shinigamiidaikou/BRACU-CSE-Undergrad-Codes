def merge(a, b):
    i, j = 0, 0
    count = 0
    merged = [0]*(len(a)+len(b))
    while True:
        if a[i] == b[j]:
            merged[count] = a[i]
            merged[count + 1] = b[j]
            count += 2
            i += 1
            j += 1
        elif a[i] < b[j]:
            merged[count] = a[i]
            count +=1
            i += 1
        else:
            merged[count] = b[j]
            count +=1 
            j += 1
        if i == len(a) or j == len(b):
            break
        
    if i == len(a):
        while j < len(b):
            merged[count] = b[j]
            j += 1
            count +=1
    elif j == len(b):
        while i < len(a):
            merged[count] = a[i]
            i += 1
            count +=1
    return merged


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[:mid])
        a2 = mergeSort(arr[mid:])
        return merge(a1, a2)


in_file = open("input3.txt")
n = int(in_file.readline())
numList = [int(x) for x in in_file.readline().split()]
in_file.close()

merged = mergeSort(numList)

out_file = open("output3.txt", "w")
out_file.write(str(merged[0]))
for i in range(1, n):
    out_file.write(" "+str(merged[i]))
out_file.close()