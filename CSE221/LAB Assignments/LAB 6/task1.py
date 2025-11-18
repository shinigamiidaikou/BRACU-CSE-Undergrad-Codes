from Graph import Graph
import heapq

def Dijkstra(G, s):
	pQ = []
	pQ.append(s)
	heapq.heapify(pQ)
	G.initializeProperties(1,2,3)
	s.distance = 0
	while len(pQ) != 0:
		u = heapq.heappop(pQ)
		for v, w in G.adjacent[str(u)]:
			tempD = u.distance + w
			if tempD < v.distance:
				v.distance = tempD
				heapq.heappush(pQ, v)
				v.parent = u
	dist = []
	for v in G.vertices:
		dist.append(v.distance if v.distance != float('inf') else '-1' )
	return " ".join([str(num) for num in dist])


inputs = 3
for i in range(2, inputs):
	in_file = open(f"input1_{i+1}.txt")
	n, m = [int(num) for num in in_file.readline().split()]
	G = Graph()
	for j in range(n):
		G.addVertex(j+1)
	for j in range(m):
		line = in_file.readline()
		u, v, w = [int(num) for num in line.split()]
		G.addEdge(u, v, w)
	sNum = in_file.readline().strip()
	s = G.vertexAddress[sNum]
	out_file = open(f"output1_{i+1}.txt", "w")
	output = Dijkstra(G, s)
	out_file.write(output)
	out_file.close()
