def countSort(arr):
    output = [0]*len(arr)
    maxval = max(arr)
    minval = min(arr)
    diff = 0
    if minval < 0:
        diff = -minval
    k = int(10*round(diff + maxval, 1) + 1)
    counter = [0]*k
    for i in range(len(arr)):
        j = int(10*round(arr[i] + diff, 1))
        counter[j] += 1
    for i in range(1, k):
        counter[i] += counter[i-1]
    for i in range(len(arr)-1,-1,-1):
        j = int(10*round(arr[i] + diff, 1))
        output[counter[j] - 1] = arr[i]
        counter[j] -= 1
    return output


arr = [2, 5, 1.2, 6.7, 1.7, 9.3, 2.2, 7.7, 0, -4, -5.1, 2, 5, 5.2]
print("functioned  :", countSort(arr))
print("correct sort:", sorted(arr))
