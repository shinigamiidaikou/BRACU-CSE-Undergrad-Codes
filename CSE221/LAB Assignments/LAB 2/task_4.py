def findMax(arr):
    if len(arr) <= 1:
        return arr[0]
    else:
        mid = len(arr)//2
        num1 = findMax(arr[:mid])
        num2 = findMax(arr[mid:])
        if num1 > num2:
            return num1
        return num2


in_file = open("input4.txt")
n = int(in_file.readline())
numList = [int(x) for x in in_file.readline().split()]
in_file.close()

out_file = open("output4.txt", "w")
out_file.write(str(findMax(numList)))
out_file.close()


#========================
# Time complexity = O(N)