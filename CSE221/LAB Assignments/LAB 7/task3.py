class Node:
    def __init__(self, val):
        self.value = val
        self.parent = self


class DisjointSet:
    def __init__(self, n) -> None:
        self.nodes = [None]*(n+1)
        self.rootSizes = [1]*(n+1)
    def findRoot(self, n):
        if n.parent == n:
            return n
        n.parent = self.findRoot(n.parent)
        return n.parent
    def unite(self, a, b):
        rootA = self.findRoot(a)
        rootB = self.findRoot(b)
        if rootA == rootB:
            return
        rootB.parent = rootA
        self.rootSizes[rootA.value] += self.rootSizes[rootB.value]
        self.rootSizes[rootB.value] = 0
    def getRootSize(self, n):
        repN = self.findRoot(n)
        return str(self.rootSizes[repN.value])
    def printRepresentatives(self):
        print([self.findRoot(node).value for node in self.nodes[1:]])


numOfInputs = 2
for i in range(numOfInputs):
    in_file = open(f"input3_{i+1}.txt")
    out_file = open(f"output3_{i+1}.txt", "w")
    n, k = [int(num) for num in in_file.readline().split()]
    friends = DisjointSet(n)
    for j in range(1, n+1):
        # Storing Nodes According to Value:Index
        friends.nodes[j] = Node(j)
    for j in range(k):
        a, b = [int(num) for num in in_file.readline().split()]
        a = friends.nodes[a]
        b = friends.nodes[b]
        friends.unite(a,b)
        out_file.write(friends.getRootSize(a)+"\n")
    in_file.close()
    out_file.close()
