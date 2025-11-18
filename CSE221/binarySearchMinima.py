def binarySearch(arr):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = (l+r) // 2
        if arr[mid-1] > arr[mid] and arr[mid] < arr[mid+1]:
            return arr[mid]
        elif arr[mid] > arr[mid+1]:
            l = mid + 1
        else:
            r = mid - 1


inp_arr = [11,9,8,7,0,2,3,5,6,12,19,20]
print(binarySearch(inp_arr))
