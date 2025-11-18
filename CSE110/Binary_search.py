def binary_search(sorted_object, element):
    sorted_object.sort()
    print("Sorted List:", sorted_object)
    left_index = 0
    right_index = len(sorted_object) - 1
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        if sorted_object[mid_index] == element:
            return mid_index
        elif sorted_object[mid_index] > element:
            right_index = mid_index - 1
        else:
            left_index = mid_index + 1
    return None


index = binary_search([50, 100, 45, 200, 356, 250, 300, 20], 200)

if index is None:
    print("Element not found")
else:
    print(f"Element found at index {index}")
