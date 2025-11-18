def kthSmallest(arr, k):
    if k >= len(arr):
        return None
    for piv in range(len(arr)):
        x = arr[piv]
        i = 0
        repitition = 0
        for j in range(len(arr)):
            if j != piv:
                if arr[j] <= x:
                    if arr[j] == x:
                        repitition += 1
                    i += 1
            if i == piv:
                i += 1
        if i < piv:
            i += 1
        if i >= k and k >= (i - repitition):
            return x


in_file = open("input4.txt")
n = int(in_file.readline().split(" // ")[0])
numList = [int(_) for _ in in_file.readline().split()]
q = int(in_file.readline().split(" // ")[0])
queries = []
for line in in_file:
    queries.append(int(line))
in_file.close()

out_file = open("output4.txt", "w")
for i in range(q):
	output = kthSmallest(numList, queries[i])
	print(output)
	out_file.write(str(output)+"\n")
out_file.close()
