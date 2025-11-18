summ_pLayer1 = 0
summ_pLayer2 = 0
summ_pLayer3 = 0
summ_pLayer4 = 0

while True:

	pLayer1_roLL = int(input("Player 1: "))
	summ_pLayer1 += pLayer1_roLL
	if summ_pLayer1 == 25:
		print("Player 1 wins")
		break
	elif summ_pLayer1 > 25:
		summ_pLayer1 -= pLayer1_roLL
	elif summ_pLayer2 != 10 or summ_pLayer2 != 20:
		if summ_pLayer1 == summ_pLayer2:
			summ_pLayer2 = 0
			print(f"Position of Player 1 now: {summ_pLayer1}")
			print(f"Position of Player 2 now: {summ_pLayer2}")
			print("Player 2 Falls back to 0")
			break

	pLayer2_roLL = int(input("Player 2: "))
	summ_pLayer2 += pLayer2_roLL
	if summ_pLayer2 == 25:
		print("Player 2 wins")
		break
	elif summ_pLayer2 > 25:
		summ_pLayer2 -= pLayer2_roLL
	if summ_pLayer1 != 10 or summ_pLayer1 != 20:
		if summ_pLayer1 == summ_pLayer2:
			summ_pLayer1 = 0
			print(f"Position of Player 1 now: {summ_pLayer1}")
			print(f"Position of Player 2 now: {summ_pLayer2}")
			print("Player 1 Falls back to 0")

			break

	print(f"Position of Player 1 now: {summ_pLayer1}")
	print(f"Position of Player 2 now: {summ_pLayer2}")
