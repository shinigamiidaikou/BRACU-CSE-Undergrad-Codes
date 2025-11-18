class Vertex:
	def __init__(self, num, colour=0):
		self.num = num
		self.colour = colour


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
	
	def initializeColour(self):
		for v in self.vertices:
			v.colour = 0