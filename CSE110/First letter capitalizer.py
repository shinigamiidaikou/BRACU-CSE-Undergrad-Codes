string = input()

############################################################
# while Loop (Manual Iteration Altering):
############################################################

# if 97 <= ord(string[0]) <= 122:
# 	print(chr(ord(string[0]) - 32), end="")
# else:
# 	print(string[0])

# i = 1
# while i < len(string):
# 	if string[i] == " " and 97 <= ord(string[i+1]) <= 122:
#		 print(" "+chr(ord(string[i+1]) - 32), end="")
#		 i += 2
#	 else:
#		 print(string[i], end="")
#		 i += 1

############################################################
# for Loop (Auto, [continue argument used]
############################################################

if 97 <= ord(string[0]) <= 122:
	print(chr(ord(string[0]) - 32), end="")
else:
	print(string[0], end="")

for i in range(1, len(string)):
	if string[i-1] == " ":
		if 65 <= ord(string[i]) <= 90:
			print(string[i], end="")
		else:
			print(chr(ord(string[i]) - 32), end="")
	else:
		print(string[i], end="")
