num1 = input()
num2 = input()

string1_even=""
string1_odd=""
string2_even=""
string2_odd=""

for char in num1:
    if ord(char) % 2 == 0:
        string1_even += char
    else:
        string1_odd += char

for char in num2:
    if ord(char) % 2 == 0:
        string2_even += char
    else:
        string2_odd += char

print("First New Number: {}".format(string1_even+string2_odd))
print("Second New Number: {}".format(string1_odd+string2_even))

summ = int(string1_even+string2_odd) + int(string1_odd+string2_even)

print("Summation of newly created two number: {}".format(summ))