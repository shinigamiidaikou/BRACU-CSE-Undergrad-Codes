def linear_search(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return i
    return -1


List = [1, 2, 3, 4, 5, 6, 7, 8]

if linear_search(List, 5) == -1:
    print("Element not found")
else:
    print(f"Element found at index {linear_search(List, 5)}")
