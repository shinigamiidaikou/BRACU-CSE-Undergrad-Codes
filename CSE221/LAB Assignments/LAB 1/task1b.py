def calculate(num1, operator, num2):
	if operator == "+":
		return num1 + num2
	elif operator == "-":
		return num1 - num2
	elif operator == "*":
		return num1 * num2
	elif operator == "/":
		return num1 / num2


in_file = open("input1b.txt")
out_file = open("output1b.txt", "w")

t = int(in_file.readline())

for i in range(t):
	s = in_file.readline().strip().split()
	out_file.write(f"The result of {s[1]} {s[2]} {s[3]} is {calculate(int(s[1]), s[2], int(s[3]))}\n")


in_file.close()
out_file.close()