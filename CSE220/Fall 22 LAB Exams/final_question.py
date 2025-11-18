def powerOf4(n):
	if n == 0:
		return False
	if n == 1:
		return True
	if (n / 4 == 1.0) or (n / 4 == -1.0):
		return True
	else:
		if n % 4 == 0:
			return powerOf4(n/4)
		return False

print("For powers of 4:")
for i in range(1, 15):
	print(powerOf4(-(4**i)))
for i in range(0, 15):
	print(powerOf4(4**i))

print("For not powers of 4:")
print(powerOf4(0))
print(powerOf4(3))
print(powerOf4(5))
print(powerOf4(45))
print(powerOf4(12))
print(powerOf4(467))
