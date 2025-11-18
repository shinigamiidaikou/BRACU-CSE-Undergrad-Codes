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
		for v in G.adjacent[str(u)]:
			v = v[0]
			tempD = u.distance + G.edgeWeight(u,v)
			if tempD < v.distance:
				v.distance = tempD
				heapq.heappush(pQ, v)
				v.parent = u
	dist = []
	for v in G.vertices:
		dist.append(v.distance)
	return dist


def shortestMeet(G, s, t):
	dist1 = Dijkstra(G, s)
	dist2 = Dijkstra(G, t)
	minTime = float('inf')
	node = 0
	for i in range(len(G.vertices)):
		nodeTime = max(dist1[i], dist2[i])
		if nodeTime < minTime:
			minTime = nodeTime
			node = i
	if minTime == float('inf'):
		return "Impossible"
	return f"Time {minTime}\nNode {G.vertices[node].num}"


inputs = 3
for i in range(inputs):
	in_file = open(f"input2_{i+1}.txt")
	n, m = [int(num) for num in in_file.readline().split()]
	G = Graph()
	for j in range(n):
		G.addVertex(j+1)
	for j in range(m):
		line = in_file.readline()
		u, v, w = [int(num) for num in line.split()]
		G.addEdge(u, v, w)
	sNum, tNum = [num for num in in_file.readline().split()]
	s = G.vertexAddress[sNum]
	t = G.vertexAddress[tNum]
	out_file = open(f"output2_{i+1}.txt", "w")
	output = shortestMeet(G, s, t)
	out_file.write(output)
	out_file.close()
