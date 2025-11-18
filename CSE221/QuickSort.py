def partition(arr, piv, upperLim):
	x = arr[piv]
	i = piv
	for j in range(piv + 1, upperLim):
		if arr[j] <=+ x:
			i = i + 1
			arr[i], arr[j] = arr[j], arr[i]
	arr[piv], arr[i] = arr[i], arr[piv]
	return i


def quicksort(A, p, uppperLim):
	if p < uppperLim:
		breakPnt = partition(A, p, uppperLim)
		quicksort(A, p, breakPnt - 1)
		quicksort(A, breakPnt + 1, uppperLim)


arr = [2, 5, 1.2, 6.7, 1.7, 9.3, 2.2, 7.7, 0, -4, -5.1, 2, 5, 5.2]
print(arr)
quicksort(arr, 1, len(arr)-1)
print(arr)