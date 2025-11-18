def binarySearch(arr, item):
    l = 0
    r = len(arr) - 1
    first = -1
    while l <= r:
        mid = (l+r) // 2
        if arr[mid] == item:
            first = mid
            r = mid - 1
        elif arr[mid] < item:
            l = mid + 1
        else:
            r = mid - 1
    count = 0
    if first != -1:
        idx = first
        while arr[idx] == item:
            count += 1
            idx += 1
    return (first, count)


inp_arr = [2,3,3,3,3,3,5,8,8,9,12,12,14,17]
print(binarySearch(inp_arr, 3))
