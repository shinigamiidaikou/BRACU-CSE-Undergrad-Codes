Low_yearLimit = int(input("From: "))
high_yearLimit = int(input("To: "))

print("\nThe Leap Years are:")
for year in range(Low_yearLimit, high_yearLimit + 1):
	if year % 4 == 0 and not(year % 100 == 0):
		print(year, end="\n")
	elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
		if year == high_yearLimit:
			print(year)
		else:
			print(year, end="\n")
