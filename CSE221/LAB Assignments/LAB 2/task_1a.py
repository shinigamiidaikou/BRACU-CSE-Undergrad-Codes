in_file = open("input1.txt") # type: ignore
n, s = [int(x) for x in in_file.readline().split()]
numList = [int(x) for x in in_file.readline().split()]
in_file.close()

out_file = open("output1.txt", "w")

# O(n^2) Approach:
found = False
for i in range(n - 1):
    for j in range(i + 1, n):
        if numList[i] + numList[j] == s:
            out_file.write(f"{i + 1} {j + 1}")
            found = True
            break
    if found == True:
        break

if found == False:
    out_file.write("IMPOSSIBLE")

out_file.close()