class Vertex:
	def __init__(self, num, colour=0):
		self.num = num
		self.colour = colour
		self.parent = None
		self.distance = float('inf')
		self.inDegree = 0
		self.outDegree = 0
	
	# Comparison operations based on distance
	# Needed for built-in Heap Queue Usage
	def __lt__(self, other: object) -> bool:
		return self.distance < other.distance
	
	def __gt__(self, other: object) -> bool:
		return self.distance > other.distance
	
	def __eq__(self, other: object) -> bool:
		return self.distance == other.distance
	
	def __ne__(self, other: object) -> bool:
		return self.distance != other.distance


class Graph:
	# Adjacency List Implementation (Weighted)
	# (Updated from LABs 4 & 5)
	def __init__(self):
		self.vertexAddress = {}
		self.adjacent = {}
		self.vertices = []
	
	def addVertex(self, num):
		ver = Vertex(num)
		self.vertexAddress[str(num)] = ver
		self.vertices.append(ver)
		self.adjacent[str(ver)] = []

	def addEdge(self, num1, num2, w):
		def manageNode(num):
			ver = None
			if str(num) not in self.vertexAddress.keys():
				ver = Vertex(num)
				self.vertexAddress[str(num)] = ver
			else:
				ver = self.vertexAddress[str(num)]
			if str(ver) not in self.adjacent.keys():
				self.adjacent[str(ver)] = []
			if ver.num not in [v.num for v in self.vertices]:
				self.vertices.append(ver)
			return ver
		u = manageNode(num1)
		v = manageNode(num2)
		self.adjacent[str(u)].append((v,w))
		u.outDegree += 1
		v.inDegree += 1
	
	def edgeWeight(self, u, v):
		for ver in self.adjacent[str(u)]:
			if str(ver[0]) == str(v):
				return ver[1]

	def rebuildDegrees(self):
		self.initializeProperties(4,5)
		for u, vL in self.adjacent.items():
			for ver in self.vertices:
				if str(ver) == u:
					ver.outDegree = len(vL)
			for v in vL:
				v[0].inDegree += 1

	def initializeProperties(self, *prop):
		if len(prop) != 0:
			for v in self.vertices:
				if 1 in prop:
					v.colour = 0
				if 2 in prop:
					v.parent = None
				if 3 in prop:
					v.distance = float('inf')
				if 4 in prop:
					v.inDegree = 0
				if 5 in prop:
					v.outDegree = 0
		else:
			for v in self.vertices:
				v.colour = 0
				v.parent = None
				v.distance = float('inf')
				v.inDegree = 0
				v.outDegree = 0

	def printVertices(self):
		print(self.vertices[0].num, end="")
		for i in range(1, len(self.vertices)):
			print(f", {self.vertices[i].num}", end="")
		print("")

	def printAdjList(self):
		for ver in self.vertices:
			print(f"{ver.num}: {[(v[0].num, v[1]) for v in self.adjacent[str(ver)]]}")
