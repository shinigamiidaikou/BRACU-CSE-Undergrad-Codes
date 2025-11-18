def partition(arr, p, r):
    # Here, pivot <-- first element
	x = arr[p]
	i = p
	for j in range(p + 1, r + 1):
		if arr[j] <= x:
			i = i + 1
			arr[i], arr[j] = arr[j], arr[i]
	arr[p], arr[i] = arr[i], arr[p]
	return i


def quicksort(arr, p, r):
	if p < r:
		q = partition(arr, p, r)
		quicksort(arr, p, q - 1)
		quicksort(arr, q + 1, r)


in_file = open("input3.txt")
t = int(in_file.readline())
numList = [int(_) for _ in in_file.readline().split()]
in_file.close()

quicksort(numList, 0, len(numList)-1)

out_file = open("output3.txt", "w")
out_file.write(f"{numList[0]}")
for i in range(1, t):
	out_file.write(f" {numList[i]}")
out_file.close()
