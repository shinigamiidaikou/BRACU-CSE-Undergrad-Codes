def merge(a, b):
    i, j = 0, 0
    count = 0
    merged = [None]*(len(a)+len(b))
    while True:
        if a[i][1] == b[j][1]:
            merged[count] = a[i]
            merged[count + 1] = b[j]
            count += 2
            i += 1
            j += 1
        elif a[i][1] < b[j][1]:
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


def sortTasks(taskList) -> list:
    if len(taskList) <= 1:
        return taskList
    else:
        mid = len(taskList)//2
        a1 = sortTasks(taskList[:mid])
        a2 = sortTasks(taskList[mid:])
        merged = merge(a1, a2)
        return merged