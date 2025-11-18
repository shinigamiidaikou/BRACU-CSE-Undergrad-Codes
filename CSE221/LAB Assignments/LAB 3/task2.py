def merge(a, b):
    i = 0
    j = 0
    count = 0
    merged = [0]*(len(a)+len(b))
    maxVal = 0
    if a[i] + b[j]**2 > a[i] + b[len(b) - 1]**2:
        maxVal = a[i] + b[j]**2
    else:
        maxVal = a[i] + b[len(b) - 1]**2
    while True:
        if a[i] == b[j]:
            merged[count] = a[i]
            merged[count + 1] = b[j]
            count += 2
            i += 1
            j += 1
        elif a[i] > b[j]:
            merged[count] = a[i]
            count += 1
            i += 1
        else:
            merged[count] = b[j]
            count += 1
            j += 1
        if i == len(a) or j == len(b):
            break
    if i == len(a):
        while j < len(b):
            merged[count] = b[j]
            j += 1
            count += 1
    elif j == len(b):
        while i < len(a):
            merged[count] = a[i]
            i += 1
            count += 1
    return (merged, maxVal)


def task2Function(arr):
    if len(arr) == 1:
        return (arr, 0.1)
    else:
        mid = len(arr)//2
        a, leftMax = task2Function(arr[:mid])
        b, rightMax = task2Function(arr[mid:])
        greaterMax = None
        merged, bothMax = merge(a, b)
        if leftMax == 0.1 or rightMax == 0.1:
            if leftMax == 0.1:
                greaterMax = rightMax
            else:
                greaterMax = leftMax
        elif leftMax > rightMax:
            greaterMax = leftMax
        else:
            greaterMax = rightMax
        if bothMax > greaterMax:
            return (merged, bothMax)
        else:
            return (merged, greaterMax)


in_file = open("input2.txt")
t = int(in_file.readline())
arr = [int(_) for _ in in_file.readline().split()]
in_file.close()

out_file = open("output2.txt", "w")
out_file.write(str(task2Function(arr)[1]))
out_file.close()
