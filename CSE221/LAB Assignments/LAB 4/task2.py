from Queue import Queue
from Graph import Graph

def BFS(G,s):
	output = ""
	s.colour = 1
	Q = Queue()
	Q.enqueue(s)
	while not(Q.isEmpty()):
		u = Q.dequeue()
		output += str(u.num) + " "
		for v in G.adjacent[u]:
			if v.colour == 0:
				v.colour = 1
				Q.enqueue(v)
		u.colour = 2
	return output.rstrip()


in_file = open("input2_4.txt")
n, m = [int(num) for num in in_file.readline().split()]
adjList = [[] for _ in range(n+1)]

for line in in_file:
	u, v = [int(num) for num in line.split()]
	adjList[u].append(v)
	adjList[v].append(u)
in_file.close()

G = Graph(adjList)
s = G.vertexAddress[str(1)]

out_file = open("output2_4.txt", "w")
for vertex in G.vertexAddress.values():
	vertex.colour = 0
out_file.write(BFS(G, s))
out_file.close()
