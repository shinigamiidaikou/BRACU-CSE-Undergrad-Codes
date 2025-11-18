year = int(input())

if year % 4 == 0 and not(year % 100 == 0):
    print("A Leap Year")
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print("A leap year")
else:
    print("Not a leap year")
