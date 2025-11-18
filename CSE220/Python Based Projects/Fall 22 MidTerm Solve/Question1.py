def nonPrimeCircular(arr, size):
	nonPrime = [0]*len(arr)
	nonPrimeCount = 0;
	for i in range(size):
		divNum = 0;
		temp = arr[i];
		while temp != 0:
			if arr[i] % temp == 0:
				divNum += 1;
			temp -= 1;
		if divNum > 2:
			nonPrime[nonPrimeCount] = arr[i];
			nonPrimeCount += 1
	
	if nonPrimeCount == 0:
		print("All are prime")
	else:
		cir = [0]*nonPrimeCount
		idx = len(cir) - 1;
		for i in range(nonPrimeCount-1, -1, -1):
			cir[idx] = nonPrime[i]
			idx = (idx + 1) % len(cir)
		return cir


lin = [7, 1, 5, 15, 52, 26, 2, 3, 0, 0]
cir = nonPrimeCircular(lin, 8)
print()
print(cir, end="\n\n")

lin = [7, 1, 5, 2, 3, 0, 0]
cir = nonPrimeCircular(lin, 5)
print(cir)