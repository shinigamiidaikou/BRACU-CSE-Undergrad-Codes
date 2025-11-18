in_file = open("input1a_2.txt")
n, m = [int(_) for _ in in_file.readline().split()]
adjMat = [[0]*(n+1) for _ in range(n+1)]

for line in in_file:
    u,v,w = [int(_) for _ in line.split()]
    adjMat[u][v] = w
in_file.close()

out_file = open("output1a_2.txt", "w")
for _ in adjMat:
    output = str(_).replace(",","")
    out_file.write(output[1:-1]+"\n")
out_file.close()
