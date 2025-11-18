
in_file = open("input8_1.txt")
out_file = open("output8_1.txt", "w")

T = int(in_file.readline().strip())
for i in range(T):
	n = int(in_file.readline().strip())
	G = Graph()
	for j in range(n):
		line = in_file.readline()
		u, v = [int(num) for num in line.split()]
		G.addEdge(u, v)
		G.addEdge(v, u)

	G.initializeAll()
	s = G.vertices[0]
	output = maxCase(G, s)
	print(f"Case {i+1}: {output}")
	out_file.write(f"Case {i+1}: {output}")

in_file.close()
out_file.close()