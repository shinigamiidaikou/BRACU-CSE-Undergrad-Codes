# Part 1: Calculate the mean of the array
def calculate_mean(arr):
    sum = 0
    for num in arr:
        sum += num
    mean = sum / len(arr)
    return mean

# Part 2: Calculate the sample standard deviation of the array
def calculate_standard_deviation(arr):
    mean = calculate_mean(arr)
    sum_squared_diff = 0
    for num in arr:
        diff = num - mean
        sum_squared_diff += diff ** 2
    variance = sum_squared_diff / (len(arr) - 1)
    print(variance)
    std_deviation = variance ** 0.5
    return std_deviation

# Part 3: Create a new array with numbers at least 1.5 standard deviations away from the mean
def create_new_array(arr):
    mean = calculate_mean(arr)
    std_deviation = calculate_standard_deviation(arr)
    temp_arr = [0]*len(arr)
    count = 0
    for num in arr:
        if abs(num - mean) >= 1.5 * std_deviation:
            temp_arr[count] = num
            count += 1
    new_arr = [0]*count
    for i in range(count):
        new_arr[i] = temp_arr[i]
    return new_arr


# Example usage
numbers = [10, 8, 13, 9, 14, 25, -5, 20, 7, 7, 4]
mean = calculate_mean(numbers)
std_deviation = calculate_standard_deviation(numbers)
new_array = create_new_array(numbers)

print("The mean of the numbers is:", mean)
print("The standard deviation is:", std_deviation)
print("New array:", new_array)