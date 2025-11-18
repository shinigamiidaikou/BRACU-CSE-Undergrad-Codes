in_file = open("input1b_3.txt")
n, m = [int(_) for _ in in_file.readline().split()]
adjList = [[] for i in range(n+1)]

for line in in_file:
	u,v,w = [int(_) for _ in line.split()]
	adjList[u].append((v,w))
in_file.close()

out_file = open("output1b_3.txt", "w")
for i in range(len(adjList)):
	output = [str(_) for _ in adjList[i]]
	out_file.write(f"{i} : {' '.join(output)}\n")
out_file.close()
