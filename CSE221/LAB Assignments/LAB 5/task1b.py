from Graph import Graph
from Queue import Queue

def topologicalSortBFS(G):
	G.initializeProperties(1)
	remaining = len(G.vertices)
	output = ""
	Q = Queue()
	for v in G.vertices:
		if v.inDegree == 0:
			Q.enqueue(v)
	while not(Q.isEmpty()):
		src = Q.dequeue()
		remaining -= 1
		output += " " + str(src.num)
		for v in G.adjacent[src]:
			v.inDegree -= 1
			if v.inDegree == 0:
				Q.enqueue(v)
	G.rebuildDegrees()
	if remaining != 0:
		return "IMPOSSIBLE"
	return output.strip()


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
	out_file = open(f"output1b_{i+1}.txt", "w")
	output = topologicalSortBFS(G)
	out_file.write(output)
	out_file.close()
