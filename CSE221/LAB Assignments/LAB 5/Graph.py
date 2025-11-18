class Vertex:
	def __init__(self, num, colour=0):
		self.num = num
		self.colour = colour
		self.parent = None
		self.inDegree = 0
		self.outDegree = 0


class Graph:
	# Adjacency List Implementation
	# (Updated from my LAB4)
	def __init__(self):
		self.vertexAddress = {}
		self.adjacent = {}
		self.ReverseAdjacent = {}
		self.vertices = []
	
	def addVertex(self, num):
		ver = Vertex(num)
		self.vertexAddress[str(num)] = ver
		self.vertices.append(ver)
		self.adjacent[ver] = []
		self.ReverseAdjacent[ver] = []
	
	def addEdge(self, num1, num2):
		
		def manageNode(num):
			ver = None
			if str(num) not in self.vertexAddress.keys():
				ver = Vertex(num)
				self.vertexAddress[str(num)] = ver
			else:
				ver = self.vertexAddress[str(num)]
			if ver not in self.adjacent.keys():
				self.adjacent[ver] = []
			if ver not in self.ReverseAdjacent.keys():
				self.ReverseAdjacent[ver] = []
			if ver not in self.vertices:
				self.vertices.append(ver)
			return ver
		
		u = manageNode(num1)
		v = manageNode(num2)
		self.adjacent[u].append(v)
		self.ReverseAdjacent[v].append(u)
		u.outDegree += 1
		v.inDegree += 1
	
	def rebuildDegrees(self):
		self.initializeProperties(3,4)
		for u, vL in self.adjacent.items():
			u.outDegree = len(vL)
			for v in vL:
				v.inDegree += 1

	def initializeProperties(self, *prop):
		if len(prop) != 0:
			for v in self.vertices:
				if 1 in prop:
					v.colour = 0
				if 2 in prop:
					v.parent = None
                if 3 in prop:
					v.inDegree = 0
                if 4 in prop:
					v.outDegree = 0
		else:
			for v in self.vertices:
				v.colour = 0
				v.parent = None
				v.inDegree = 0
				v.outDegree = 0

	def printVertices(self):
		print(self.vertices[0].num, end="")
		for i in range(1, len(self.vertices)):
			print(f", {self.vertices[i].num}", end="")
		print("")

	def printAdjList(self):
		for ver in self.vertices:
			print(f"{ver.num}: {[v.num for v in self.adjacent[ver]]}")
	
	def printReverseAdjList(self):
		for ver in self.vertices:
			print(f"{ver.num}: {[v.num for v in self.ReverseAdjacent[ver]]}")