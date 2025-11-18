from Graph_22101621 import Graph
from Queue_22101621 import Queue

def maxCase(G, s):
	temp = G.vertices.copy()
	disjointLevelCount = {"1" : [0]*len(G.vertices)}
	s.colour = 1
	Q = Queue()
	Q.enqueue(s)
	disjoint = 1
	while not(Q.isEmpty()):
		u = Q.dequeue()
		temp.remove(u)
		disjointLevelCount[str(disjoint)][u.discovery] += 1
		for v in G.adjacent[u]:
			if v.colour == 0:
				v.colour = 1
				v.parent = u
				v.discovery = u.discovery + 1
				Q.enqueue(v)
		u.colour = 2
		if Q.isEmpty():
			if len(temp) != 0:
				disjoint += 1
				disjointLevelCount[str(disjoint)] = [0]*len(temp)
				Q.enqueue(temp[0])
				temp[0].colour = 1
	maxTotal = 0
	for cList in disjointLevelCount.values():
		oddLevelSum = 0
		evenLevelSum = 0
		i = 0
		while i < len(cList) - 1:
			if cList[i] == 0:
				break
			evenLevelSum += cList[i]
			oddLevelSum += cList[i+1]
			i += 2
		if (len(cList)-1) % 2 == 0:
			evenLevelSum += cList[-1]
		maxTotal += max(evenLevelSum, oddLevelSum)
	return maxTotal


T = int(input())
for i in range(T):
	n = int(input())
	G = Graph()
	for j in range(n):
		u, v = [int(num) for num in input().split()]
		G.addEdge(u, v)
		G.addEdge(v, u)

	G.initializeAll()
	s = G.vertices[0]
	output = maxCase(G, s)
	print(f"Case {i+1}: {output}")
