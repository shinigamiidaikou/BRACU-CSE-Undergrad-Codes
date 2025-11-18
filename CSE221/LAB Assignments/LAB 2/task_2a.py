in_file = open("input2.txt")
n = int(in_file.readline())
list1 = [int(x) for x in in_file.readline().split()]
m = int(in_file.readline())
list2 = [int(x) for x in in_file.readline().split()]
in_file.close()

merged = list1 + list2
merged.sort()
out_file = open("output2.txt", "w")
out_file.write(str(merged[0]))
for i in range(1, n+m):
    out_file.write(" "+str(merged[i]))
out_file.close()