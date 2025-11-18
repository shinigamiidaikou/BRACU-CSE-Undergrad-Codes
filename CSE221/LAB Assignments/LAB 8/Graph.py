class Vertex:
	def __init__(self, num, colour=0):
		self.num = num
		self.colour = colour
		self.primsKey = float('inf')
		self.parent = None
		self.inDegree = 0
		self.outDegree = 0
	
	def __hash__(self):
		return hash(str(self))
	# Object Value Comparison against primsKey
	def __eq__(self, object) -> bool:
		return self.primsKey == object.primsKey
	def __ne__(self, object) -> bool:
		return self.primsKey != object.primsKey
	def __gt__(self, object) -> bool:
		return self.primsKey > object.primsKey
	def __lt__(self, object) -> bool:
		return self.primsKey < object.primsKey


class Graph:
	# Adjacency List Implementation (Weighted)
	# (Similar to LABs 5 & 6)
	def __init__(self):
		self.vertexAddress = {}
		self.adjacent = {}
		self.vertices = []
	
	def addVertex(self, num):
		ver = Vertex(num)
		self.vertexAddress[num] = ver
		self.vertices.append(ver)
		self.adjacent[ver] = []

	def addEdge(self, num1, num2, w):
		def manageNode(num):
			ver = None
			if num not in self.vertexAddress.keys():
				ver = Vertex(num)
				self.vertexAddress[num] = ver
			else:
				ver = self.vertexAddress[num]
			if ver not in self.adjacent.keys():
				self.adjacent[ver] = []
			if ver not in self.vertices:
				self.vertices.append(ver)
			return ver
		u = manageNode(num1)
		v = manageNode(num2)
		self.adjacent[u].append((v,w))
		u.outDegree += 1
		v.inDegree += 1
	
	def edgeWeight(self, u, v):
		for ver in self.adjacent[u]:
			if ver[0] == v:
				return ver[1]

	def rebuildDegrees(self):
		self.initializeProperties(4,5)
		for u, vL in self.adjacent.items():
			u.outDegree = len(vL)
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
					v.primsKey = float('inf')
				if 4 in prop:
					v.inDegree = 0
				if 5 in prop:
					v.outDegree = 0
		else:
			for v in self.vertices:
				v.colour = 0
				v.parent = None
				v.primsKey = float('inf')
				v.inDegree = 0
				v.outDegree = 0

	def printVertices(self):
		print(self.vertices[0].num, end="")
		for i in range(1, len(self.vertices)):
			print(f", {self.vertices[i].num}", end="")
		print("")

	def printAdjList(self):
		for ver in self.vertices:
			print(f"{ver.num}: {[(v[0].num, v[1]) for v in self.adjacent[ver]]}")
