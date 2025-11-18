string = input()
delete = input()
new_string = str()

for char in string:
	if char in delete or chr(ord(char)+32) in delete:
		pass
	else:
		new_string += char

print(new_string)
