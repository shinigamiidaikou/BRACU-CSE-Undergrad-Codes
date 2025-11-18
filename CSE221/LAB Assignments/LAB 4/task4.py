from Graph import Graph

def cycleExists(G,u):
	u.colour = 1
	cycleFound = False
	for v in G.adjacent[u]:
		if cycleFound:
			break
		if v.colour == 0:
			cycleFound = cycleExists(G,v)
		elif v.colour == 1:
			cycleFound = True
	u.colour = 2
	return cycleFound


in_file = open("input4_4.txt")
n, m = [int(num) for num in in_file.readline().split()]
adjList = [[] for _ in range(n+1)]

for line in in_file:
	u, v = [int(num) for num in line.split()]
	adjList[u].append(v)
in_file.close()

G = Graph(adjList)
s = G.vertexAddress[str(1)]

out_file = open("output4_4.txt", "w")
for vertex in G.vertexAddress.values():
	vertex.colour = 0
if cycleExists(G,s):
	out_file.write("YES")
else:
	out_file.write("NO")
out_file.close()
