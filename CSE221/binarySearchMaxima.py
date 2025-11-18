def binarySearch(arr):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = (l+r) // 2
        if arr[mid-1] < arr[mid] and arr[mid] > arr[mid+1]:
            return arr[mid]
        elif arr[mid] < arr[mid+1]:
            l = mid + 1
        else:
            r = mid - 1


inp_arr = [int(x) for x in "1, 3, 4, 5, 9, 6, 2, -1".split(", ")]
print(inp_arr)
print(binarySearch(inp_arr))