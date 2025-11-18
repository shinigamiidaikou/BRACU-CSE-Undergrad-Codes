class Vertex:
	def __init__(self, num, colour=0):
		self.num = num
		self.colour = colour
		self.parent = None
		self.discovery = 0


class Graph:
	# Adjacency List Implementation
	def __init__(self, adjList):
		self.vertexAddress = {}
		self.adjacent = {}
		for i in range(1, len(adjList)):
			u = None
			if str(i) not in self.vertexAddress.keys():
				u = Vertex(i)
				self.vertexAddress[str(i)] = u
			else:
				u = self.vertexAddress[str(i)]
			self.adjacent[u] = []
			for j in adjList[i]:
				v = None
				if str(j) not in self.vertexAddress.keys():
					v = Vertex(j)
					self.vertexAddress[str(j)] = v
				else:
					v = self.vertexAddress[str(j)]
				self.adjacent[u].append(v)
		self.vertices = list(self.vertexAddress.values())
	
	def initializeAll(self):
		for v in self.vertices:
			v.colour = 0
			v.discovery = 0
			v.parent = None

	def printVertices(self):
		print(self.vertices[0].num, end="")
		for i in range(1, len(self.vertices)):
			print(f", {self.vertices[i].num}", end="")
		print("")
	def printAdjList(self):
		for i in range(1, len(self.vertices)):
			print(f"{i}: {[v.num for v in self.adjacent[self.vertexAddress[str(i)]]]}")
