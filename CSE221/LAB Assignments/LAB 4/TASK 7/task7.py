from Graph_22101621 import Graph

def modDFS(G, a, b):
	a.colour = 1
	found = False
	count = 0
	for v in G.adjacent[a]:
		if v == b:
			found = True
			break
		if v.colour == 0:
			v.colour = 1
			count = modDFS(G, v, b)
		if count >= 1:
			return 1 + count
	if found:
		return 1
	return 0


def longestPath(G):
	maxCount = 0
	A = G.vertices[0]
	B = G.vertices[1]
	for i in range(len(G.vertices)-1):
		for j in range(i + 1, len(G.vertices)):
			a = G.vertices[i]
			b = G.vertices[j]
			G.initializeColour()
			count = modDFS(G, a, b)
			if count > maxCount:
				maxCount = count
				A = a
				B = b
	return sorted([A.num, B.num])


in_file = open("input7_1.txt")
n = int(in_file.readline().strip())
adjList = [[] for _ in range(n+1)]

for line in in_file:
	u, v = [int(num) for num in line.split()]
	adjList[u].append(v)
	adjList[v].append(u)
in_file.close()

G = Graph(adjList)

out_file = open("output7_1.txt", "w")
G.initializeColour()
output = longestPath(G)
out_file.write(str(output[0])+" "+str(output[1]))
out_file.close()
