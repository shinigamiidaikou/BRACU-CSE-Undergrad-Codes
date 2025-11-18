from Graph import Graph
import heapq

def lexicographicTopSort(G):
	pQ = []
	heapq.heapify(pQ)
	for v in G.vertices:
		if v.inDegree == 0:
			heapq.heappush(pQ, v.num)
	G.initializeProperties(1)
	remaining = len(G.vertices)
	output = ""
	while len(pQ) != 0:
		src = G.vertexAddress[str(heapq.heappop(pQ))]
		output += " " + str(src.num)
		remaining -= 1
		for v in G.adjacent[src]:
			v.inDegree -= 1
			if v.inDegree == 0:
				heapq.heappush(pQ, v.num)
	G.rebuildDegrees()
	if remaining != 0:
		return "IMPOSSIBLE"
	return output.strip()


inputs = 3
for i in range(inputs):
	in_file = open(f"input2_{i+1}.txt")
	n, m = [int(num) for num in in_file.readline().split()]
	G = Graph()
	for j in range(n):
		G.addVertex(j+1)
	for j in range(m):
		line = in_file.readline()
		u, v = [int(num) for num in line.split()]
		G.addEdge(u, v)
	out_file = open(f"output2_{i+1}.txt", "w")
	output = lexicographicTopSort(G)
	out_file.write(output)
	out_file.close()
