from Graph import Graph
import heapq

def lowestDangerValue(G, s, n, nodeLevels):
	s.colour = 1
	current = nodeLevels[s.num]
	pQ = []
	for v, w in G.adjacent[str(s)]:
		pQ.append((w, v))
	heapq.heapify(pQ)
	while len(pQ) != 0:
		w, v = heapq.heappop(pQ)
		if str(v) == str(n):
			if nodeLevels[v.num] == 0:
				nodeLevels[v.num] = max(current, w)
			else:
				dVal = max(current, w)
				nodeLevels[v.num] = min(dVal, nodeLevels[v.num])
			continue
		if v.colour == 0:
			v.parent = s
			nodeLevels[v.num] = max(current, w)
			lowestDangerValue(G, v, n, nodeLevels)
	s.colour = 2
	if s.num == 1:
		if nodeLevels[-1] == 0:
			return "Impossible"
		return str(nodeLevels[-1])


inputs = 2
for i in range(inputs):
	in_file = open(f"input3_{i+1}.txt")
	n, m = [int(num) for num in in_file.readline().split()]
	G = Graph()
	for j in range(n):
		G.addVertex(j+1)
	for j in range(m):
		line = in_file.readline()
		u, v, w = [int(num) for num in line.split()]
		G.addEdge(u, v, w)
	out_file = open(f"output3_{i+1}.txt", "w")
	start = G.vertexAddress['1']
	end = G.vertexAddress[f'{n}']
	levels = [0]*(n+1)
	output = lowestDangerValue(G, start, end, levels)
	out_file.write(output)
	out_file.close()
