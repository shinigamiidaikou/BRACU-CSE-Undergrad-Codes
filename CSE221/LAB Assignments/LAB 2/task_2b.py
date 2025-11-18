in_file = open("input2.txt")
n = int(in_file.readline())
list1 = [int(x) for x in in_file.readline().split()]
m = int(in_file.readline())
list2 = [int(x) for x in in_file.readline().split()]
in_file.close()

i, j = 0, 0
count = 0
merged = [0]*(n+m)
while True:
    if list1[i] == list2[j]:
        merged[count] = list1[i]
        count +=1 
        merged[count] = list2[j]
        count +=1 
        i += 1
        j += 1
    elif list1[i] < list2[j]:
        merged[count] = list1[i]
        count +=1 
        i += 1
    else:
        merged[count] = list2[j]
        count +=1 
        j += 1
    if i == len(list1) or j == len(list2):
        break

if i == len(list1):
    while j < len(list2):
        merged[count] = list2[j]
        j += 1
        count +=1 
elif j == len(list2):
    while i < len(list1):
        merged[count] = list1[i]
        i += 1
        count +=1

out_file = open("output2.txt", "w")
out_file.write(str(merged[0]))
for i in range(1, n+m):
    out_file.write(" "+str(merged[i]))
out_file.close()