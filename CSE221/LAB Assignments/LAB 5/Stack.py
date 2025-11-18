class Node:
	def __init__(self, elem=None, nxt=None):
		self.elem = elem
		self.next = nxt


class Stack:
	#DHSCL Implementation
	def __init__(self):
		self.top = Node() # None
	def push(self, item):
		self.top = Node(item, self.top)
	def pop(self):
		if self.top.next == None:
			return None
		topNode = self.top
		self.top = self.top.next
		return topNode.elem
	def peek(self):
		return self.top.elem
	def isEmpty(self) -> bool:
		if self.top.next == None:
			return True
		return False
	def toList(self):
		stackList = []
		n = self.top
		while n.next != None:
			stackList.append(n.elem)
			n = n.next
		return stackList
	def __str__(self) -> str:
		n = self.top
		if n.next != None:
			s = "| %-3s | <-- top\n" % (n.elem.num)
		else:
			s = ""
		n = n.next
		while n.next != None:
			s += "| %-3s |\n" % (n.elem.num)
			n = n.next
		return s + "-"*7