Limit = int(input())
total = 0

for i in range(1, Limit+1):
	item_summ = 0
	for dec in range(i):
		item_summ += 1*10**dec
	total += item_summ
	if i == Limit:
		print("1"*Limit)
	else:
		print("1"*i, "+", end=" ")

print("The Sum is:", total)
