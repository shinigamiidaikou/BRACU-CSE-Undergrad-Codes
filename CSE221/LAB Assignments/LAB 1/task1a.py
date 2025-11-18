in_file = open("input1a.txt")
out_file = open("output1a.txt", "w")

t = int(in_file.readline().strip())

for i in range(t):
    n = int(in_file.readline().strip())
    if n%2 == 0:
        out_file.write(f"{n} is an Even number.\n")
    else:
        out_file.write(f"{n} is an Odd number.\n")

in_file.close()
out_file.close()