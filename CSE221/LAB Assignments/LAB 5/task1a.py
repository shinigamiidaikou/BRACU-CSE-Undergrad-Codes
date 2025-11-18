from Graph import Graph
from Stack import Stack

def DFS(G, u, st):
	u.colour = 1
	cycleFound = False
	for v in G.adjacent[u]:
		if cycleFound:
			break
		if v.colour == 0:
			cycleFound = DFS(G,v,st)
		elif v.colour == 1:
			cycleFound = True
	u.colour = 2
	st.push(u.num)
	return cycleFound


def topologicalSort(G):
	st = Stack()
	G.initializeProperties(1)
	cycleExists = False
	for v in G.vertices:
		if cycleExists:
			return "IMPOSSIBLE"
		if v.colour == 0:
			cycleExists = DFS(G, v, st)
	topSort = [str(num) for num in st.toList()]
	return " ".join(topSort)


inputs = 3
for i in range(inputs):
	in_file = open(f"input1_{i+1}.txt")
	n, m = [int(num) for num in in_file.readline().split()]
	G = Graph()
	for j in range(n):
		G.addVertex(j+1)
	for j in range(m):
		line = in_file.readline()
		u, v = [int(num) for num in line.split()]
		G.addEdge(u, v)
	out_file = open(f"output1a_{i+1}.txt", "w")
	output = topologicalSort(G)
	out_file.write(output)
	out_file.close()
