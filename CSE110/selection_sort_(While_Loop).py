L1 = [50, 100, 45, 200, 356, 250, 300, 20]

i = 0
while i<(len(L1)-1):
	minIndex = i
	j = i + 1
	while j < len(L1):
		if L1[minIndex] > L1[j]:
			minIndex = j
		j += 1
	temp = L1[i]
	L1[i] = L1[minIndex]
	L1[minIndex] = temp
	i += 1

print(L1)