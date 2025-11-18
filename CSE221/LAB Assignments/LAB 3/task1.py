def merge(a, b):
    i = 0
    j = 0
    count = 0
    merged = [0]*(len(a)+len(b))
    lowerCount = 0
    while True:
        if a[i] == b[j]:
            merged[count] = a[i]
            merged[count + 1] = b[j]
            count += 2
            i += 1
            j += 1
        elif a[i] > b[j]:
            merged[count] = a[i]
            lowerCount += len(b[j:])
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
    return (merged, lowerCount)


def lowerHeightCounter(arr):
    if len(arr) == 1:
        return arr, 0
    else:
        mid = len(arr)//2
        a, leftCount = lowerHeightCounter(arr[:mid])
        b, rightCount = lowerHeightCounter(arr[mid:])
        merged, bothCount = merge(a, b)
        return (merged, leftCount + rightCount + bothCount)


in_file = open("input1.txt")
t = int(in_file.readline())
aliens = [int(_) for _ in in_file.readline().split()]
in_file.close()

out_file = open("output1.txt", "w")
newArr, count = lowerHeightCounter(aliens)
out_file.write(str(count))
out_file.close()
