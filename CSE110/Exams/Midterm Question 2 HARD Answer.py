num1 = int(input())
num2 = int(input())

temp = num1
counter = 0
while temp != 0:
    temp //= 10
    counter+=1

power = counter - 1
string1_even=""
string1_odd=""
for i in range(counter):
    digit = num1 // (10**power)
    num1 %= 10**power
    power -= 1
    if digit % 2 == 0:
        string1_even+=str(digit)
    else:
        string1_odd+=str(digit)

temp = num2
counter = 0
while temp != 0:
    temp //= 10
    counter+=1

power = counter - 1
string2_even=""
string2_odd=""
for i in range(counter):
    digit = num2 // (10**power)
    num2 %= 10**power
    power -= 1
    if digit % 2 == 0:
        string2_even+=str(digit)
    else:
        string2_odd+=str(digit)

print("First New Number: {}".format(string1_even+string2_odd))
print("Second New Number: {}".format(string1_odd+string2_even))

summ = int(string1_even+string2_odd) + int(string1_odd+string2_even)

print("Summation of newly created two number: {}".format(summ))