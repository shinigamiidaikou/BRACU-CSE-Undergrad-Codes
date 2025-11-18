from Graph import Graph
from Stack import Stack

def DFS(G, u, st, reverse=False):
	u.colour = 1
	if reverse:
		for v in G.ReverseAdjacent[u]:
			if v.colour == 0:
				DFS(G, v, st, reverse=True)
		st.push(u)
	else:
		for v in G.adjacent[u]:
			if v.colour == 0:
				DFS(G, v, st)
		st.push(u)
	u.colour = 2


def topSort(G):
	st = Stack()
	G.initializeProperties(1)
	for v in G.vertices:
		if v.colour == 0:
			DFS(G, v, st)
	return st


def sCC(G):
	st = topSort(G)
	sccList = []
	G.initializeProperties(1)
	while not(st.isEmpty()):
		tempSt = Stack()
		u = st.pop()
		if u.colour == 0:
			DFS(G, u, tempSt, reverse=True)
			sccList.append(tempSt)
	for i in range(len(sccList)):
		sccList[i] = sorted([str(ver.num) for ver in sccList[i].toList()])
	return sorted(sccList)


inputs = 3
for i in range(inputs):
	in_file = open(f"input3_{i+1}.txt")
	n, m = [int(num) for num in in_file.readline().split()]
	G = Graph()
	for j in range(n):
		G.addVertex(j+1)
	for j in range(m):
		line = in_file.readline()
		u, v = [int(num) for num in line.split()]
		G.addEdge(u, v)
	out_file = open(f"output3_{i+1}.txt", "w")
	components = sCC(G)
	for scc in components:
		scc = " ".join(scc)
		out_file.write(scc+"\n")
	out_file.close()
