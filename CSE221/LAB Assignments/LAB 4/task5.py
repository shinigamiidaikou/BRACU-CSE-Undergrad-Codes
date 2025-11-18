from Graph import Graph
from Queue import Queue

def shortestPath(G, s, d):
	s.colour = 1
	Q = Queue()
	Q.enqueue(s)
	while not(Q.isEmpty()):
		u = Q.dequeue()
		for v in G.adjacent[u]:
			if v.colour == 0:
				v.colour = 1
				v.parent = u
				v.discovery = u.discovery + 1
				Q.enqueue(v)
		u.colour = 2
	path = str(d.num)
	v = d
	while v != s:
		v = v.parent
		path += " " + str(v.num)
	return path[-1::-1], d.discovery


in_file = open("input5_4.txt")
n, m, d = [int(num) for num in in_file.readline().split()]
adjList = [[] for _ in range(n+1)]

for line in in_file:
	u, v = [int(num) for num in line.split()]
	adjList[u].append(v)
	adjList[v].append(u)
in_file.close()

G = Graph(adjList)

s = G.vertexAddress[str(1)]
d = G.vertexAddress[str(d)]

out_file = open("output5_4.txt", "w")
G.initializeAll()
path, time = shortestPath(G, s, d)
out_file.write(f"Time: {time}\n")
out_file.write(f"Shortest Path: {path}\n")
out_file.close()
