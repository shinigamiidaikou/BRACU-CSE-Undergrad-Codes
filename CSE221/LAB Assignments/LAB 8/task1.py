from Graph import Graph
from heapq import heapify, heappop

def MST_value_prim(G, s):
    G.initializeProperties(2,3)
    s.primsKey = 0
    pQ = [v for v in G.vertices]
    heapify(pQ)
    while len(pQ) != 0:
        u = heappop(pQ) #Pops first element which is of minimum key
        for v, w in G.adjacent[u]:
            if v in pQ and w < v.primsKey:
                v.primsKey = w
                v.parent = u
        heapify(pQ) #Needed for correct heapification before next pop
    final = [v.primsKey for v in G.vertices]
    return sum(final)


inputs = 2
for i in range(inputs):
    in_file = open(f"input1_{i+1}.txt")
    n, m = [int(num) for num in in_file.readline().split()]
    G = Graph()
    for j in range(n):
        G.addVertex(j+1)
    for j in range(m):
        u, v, w = [int(num) for num in in_file.readline().split()]
        G.addEdge(u,v,w)
        G.addEdge(v,u,w)
    s = G.vertexAddress[1]
    in_file.close()
    out_file = open(f"output1_{i+1}.txt", "w")
    output = MST_value_prim(G, s)
    out_file.write(str(output))
    out_file.close()