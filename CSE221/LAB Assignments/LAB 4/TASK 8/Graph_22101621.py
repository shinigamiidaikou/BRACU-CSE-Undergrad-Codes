class Vertex:
	def __init__(self, num, colour=0):
		self.num = num
		self.colour = colour
		self.parent = None
		self.discovery = 0


class Graph:
	# Adjacency List Implementation
	def __init__(self):
		self.vertexAddress = {}
		self.adjacent = {}
		self.vertices = []
	
	def addEdge(self, num1, num2):
		u = None
		if str(num1) not in self.vertexAddress.keys():
			u = Vertex(num1)
			self.vertexAddress[str(num1)] = u
		else:
			u = self.vertexAddress[str(num1)]
		if u not in self.adjacent.keys():
			self.adjacent[u] = []
		if u not in self.vertices:
			self.vertices.append(u)
		v = None
		if str(num2) not in self.vertexAddress.keys():
			v = Vertex(num2)
			self.vertexAddress[str(num2)] = v
		else:
			v = self.vertexAddress[str(num2)]
		self.adjacent[u].append(v)
		if v not in self.vertices:
			self.vertices.append(v)

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
		for ver in self.vertices:
			print(f"{ver.num}: {[v.num for v in self.adjacent[self.vertexAddress[str(ver.num)]]]}")
	def printLevels(self):
		for ver in self.vertices:
			print(f"{ver.num}: {self.vertexAddress[str(ver.num)].discovery}")