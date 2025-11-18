def binarySearch(arr, item):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = (l+r) // 2
        print(f"l={l}, mid={mid}, r={r}")
        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            l = mid + 1
        else:
            r = mid - 1
    return -1


inp_arr = [int(x) for x in "23 2 19 3 7 11 5 13".split()]
print(inp_arr)
print(binarySearch(inp_arr, 2))
